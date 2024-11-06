video_titles = [
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]

json_videos = [{'id': 1, 'title': 'The Art of Coding'}, {'id': 2, 'title': 'Exploring the Cosmos'}, {'id': 3, 'title': 'Cooking Masterclass: Italian Cuisine'}, {'id': 4, 'title': 'History Uncovered: Ancient Civilizations'}, {'id': 5, 'title': 'Fitness Fundamentals: Strength Training'}, {'id': 6, 'title': 'Digital Photography Essentials'}, {'id': 7, 'title': 'Financial Planning for Beginners'}, {'id': 8, 'title': "Nature's Wonders: National Geographic"}, {'id': 9, 'title': 'Artificial Intelligence Revolution'}, {'id': 10, 'title': 'Travel Diaries: Discovering Europe'}]

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

merge_sort(json_videos)

print(json_videos)