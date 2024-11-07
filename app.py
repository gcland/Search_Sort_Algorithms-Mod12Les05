from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields, validate
from marshmallow import ValidationError
from sqlalchemy import select
from password import password

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://root:{password}@localhost/videos_db' 
db = SQLAlchemy(app)
ma = Marshmallow(app)

class VideoSchema(ma.Schema):
    title = fields.String(required=True)

    class Meta:
        fields = ('id','title')

video_schema = VideoSchema()
videos_schema = VideoSchema(many=True)

class Video(db.Model):
    __tablename__ = 'Videos'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)

#Example format in Postman (add/update)

# {

#     "title":"XXXXXX",

# }

@app.route('/videos', methods=['GET'])
def get_videos():   # merge sort function sorts the list alphabetically using merge sort
    videos = Video.query.all()
    json_videos = videos_schema.jsonify(videos).json
    merge_sort(json_videos)
    return json_videos

@app.route('/videos/by-id', methods=['GET']) #/by-id?id=1    (example)
def view_by_videos_id():
    id = request.args.get('id')
    video = Video.query.filter(Video.id == id).first()
    if video:
        return video_schema.jsonify(video)
    else:
        return jsonify({"message": "Customer not found"}), 404

@app.route('/videos/by-title', methods=['GET']) #/by-title?title="The Art of Coding" (example)
def view_by_video_title():
    title = request.args.get('title')
    json_videos = get_videos()
    video = binary_seach(json_videos, title)
    if video:
        return video
    else:
        return jsonify({"message": "Video not found"}), 404

def binary_seach(video_titles, title):
    low = 0 
    high = len(video_titles) - 1 
    success = False
    while low <= high:
        mid = (low+high)//2
        if ord(video_titles[mid]['title'][0]) == ord(title[0]):
            index = mid
            while ord(video_titles[mid]['title'][0]) == ord(title[0]):
                try: 
                    video_titles[index]['title']
                    if video_titles[index]['title'] == title:
                        print(f'\nTitle: "{video_titles[index]['title']}" with id: {video_titles[index]['id']}.\n')
                        title = video_titles[index]['title']
                        id = video_titles[index]['id']
                        success = True
                        break
                    else:
                        index+=1
                except IndexError:
                    print(f"'{title}' was not found.")
                    break
            if success == True:
                return {'id': id, 'title': title}
            else:
                break
            
        elif ord(video_titles[mid]['title'][0]) < ord(title[0]):
            low = mid + 1
        else:
            high = mid - 1

@app.route('/video', methods=['POST'])
def add_video():
    try:
        video_data = video_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    new_video = Video(title=video_data['title'])
    db.session.add(new_video)
    db.session.commit()
    return jsonify({'message': 'New video added successfully'}), 201

@app.route('/videos', methods=['POST']) # see example postman format below this endpoint
def add_videos():
    try:
        json_videos = request.json
        videos_list = json_videos['videos']
        # videos_list = merge_sort(json_videos['videos']) #input to sort before adding into database
        for video_title in videos_list: 
            data = {'title': video_title}
            video_data = video_schema.load(data) 
            new_video = Video(title=video_data['title'])
            db.session.add(new_video)
            db.session.commit()

    except ValidationError as err:
        return jsonify(err.messages), 400
    
    return jsonify({'message': 'New videos added successfully'}), 201    


# Example format input for inputting a list of videos
# {
#     "videos": 
#     ["Artificial Intelligence Revolution",
#     "Cooking Masterclass: Italian Cuisine",
#     "Digital Photography Essentials",
#     "Exploring the Cosmos",
#     "Financial Planning for Beginners",
#     "Fitness Fundamentals: Strength Training",
#     "History Uncovered: Ancient Civilizations",
#     "Nature's Wonders: National Geographic",
#     "The Art of Coding",
#     "Travel Diaries: Discovering Europe"
# ]
# }

def merge_sort(list):
    if len(list) > 1:
        mid = len(list)//2
        left_half = list[:mid]
        right_half = list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i]['title'] < right_half[j]['title']:
                list[k] = left_half[i]
                i+=1

            else:
                list[k] = right_half[j]
                j+=1
            k+=1
        while i < len(left_half):
            list[k] = left_half[i]
            i+=1
            k+=1
        
        while j < len(right_half):
            list[k] = right_half[j]
            j+=1
            k+=1
    return list

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
