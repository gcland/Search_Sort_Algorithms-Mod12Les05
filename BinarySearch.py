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

json_videos = [{'id': 1, 'title': 'Artificial Intelligence Revolution'}, {'id': 2, 'title': 'Cooking Masterclass: Italian Cuisine'}, {'id': 3, 'title': 'Digital Photography Essentials'}, {'id': 4, 'title': 'Exploring the Cosmos'}, {'id': 5, 'title': 'Financial Planning for Beginners'}, {'id': 6, 'title': 'Fitness Fundamentals: Strength Training'}, {'id': 7, 'title': 'History Uncovered: Ancient Civilizations'}, {'id': 8, 'title': "Nature's Wonders: National Geographic"}, {'id': 9, 'title': 'The Art of Coding'}, {'id': 10, 'title': 'Travel Diaries: Discovering Europe'}]

# Binary Search assumes list is first sorted

def binary_seach(video_titles, title): # This algorithm does not take in a list but takes in a list of objects received from database
    low = 0 
    high = len(video_titles) - 1 
    success = False
    while low <= high:
        mid = (low+high)//2
        print(video_titles[mid]['title'])
        if ord(video_titles[mid]['title'][0]) == ord(title[0]):
            index = mid
            while ord(video_titles[mid]['title'][0]) == ord(title[0]):
                try: 
                    video_titles[index]['title']
                    if video_titles[index]['title'] == title:
                        print(f'\nTitle: "{video_titles[index]['title']}" with id: {video_titles[index]['id']}.\n')
                        success = True
                        break
                    else:
                        index+=1
                except IndexError:
                    print(f"'{title}' was not found.")
                    break
            if success == True:
                return title
            else:
                break
            
        elif ord(video_titles[mid]['title'][0]) < ord(title[0]):
            low = mid + 1
        else:
            high = mid - 1

video = binary_seach(json_videos, "Travel Diaries: Discovering Europe")
print(video)


# For the worst-case largest lists:
# Secondary idea: instead of having a linear check @ 'while ord(video_titles[mid][0]) == ord(title[0]):',
# do:
# secondCharList = []
# while ord(video_titles[mid][0]) == ord(title[0]):
#   secondCharList.append(video_titles[index][1:]) # remove first character
#   secondCharList.sort()   # List must be sorted 
#   < repeat the binary search function > 
#   Could potentially repeat this infinitely

# This time complexity for largests lists should be faster than a linear search, but this increases the space complexity 
# because we are creating a new sublist with each sub-binary search 
