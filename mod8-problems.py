'''
#1. Create a file called gardening_tips.txt and add at least 3 gardening tips to it.
    Write a Python script that reads a file gardening_tips.txt and prints
    out each tip one by one.
'''

gardenfile = open("gardening_tips.txt", "w")
gardenfile.write("1. Make sure to use fertile soil.\n")
gardenfile.write("2. Most plants need at least 6 hours of sun to thrive.\n")
gardenfile.write("3. Water and feed your plants regularly.\n")
gardenfile.close()
gardenfile = open("gardening_tips.txt", "r")
content = gardenfile.read()
print(content) # I'm not sure if this is the *most* efficent code but it works!
gardenfile.close()
print() #seperates functions

'''
#2. Write a Python program that allows users to log their hiking trips. The program should:
    - Use a while loop to repeatedly ask for a hike name and distance in miles
    - Save each entry to hiking_log.txt (each hike on a new line)
    - When the user presses 0, exit the loop & print the contents of hiking_log.txt
'''

hiking_log = open("hiking_log.txt", "w")
hiking_log.write("")
hiking_log.close() #used for clearing previous codes like during lesson

hiking_log = open("hiking_log.txt", "a")
while True:
    hike = input("Enter the name of the hike (enter 0 to exit). ")
    if hike == "0":
        break

    distance = input("Enter distance hiked in miles: ") # didn't put an exit here as if there is a hike there is a distance.
    hiking_log.write(hike + "\t" + distance + "\n")
hiking_log.close()

hikes = {}
with open("hiking_log.txt", "r") as file:
    for line in file:
        stripped_line = line.strip()
        hike, distance = stripped_line.split("\t")
        hikes[hike] = distance
print(hikes)
hiking_log.close()
print() #seperates functions

'''
#3. Create a text file called song_lyrics.txt and copy the lyrics of a song into it. Write a Python program that:
    - Reads the file
    - Requests 5 inputs from the user: 5 words the user would like to count the frequency of
    - Counts how many times each word appears
    - Creates a dictionary of the words and their counts
    - Print the dictionary to the console
'''

song = open("song_lyrics.txt", "r")
lyrics = song.read().lower()
song.close()

user_words = []
for i in range(5):
    word = input("Enter a word to count (press enter after each word): ").lower()
    user_words.append(word)

word_counts = {}
for word in user_words:
    count = lyrics.count(word)
    word_counts[word] = count
print(word_counts)
print() #seperates functions
# I imagine there was a simpler way of doing this one but I was struggling

'''
#4. Create a poll.txt file that contains a list of "yea" or "nay" votes separated by commas.
    Write a program that reads the poll.txt file
    Count how many votes "yea" or "nay" received and print the results.
'''

polls = open("poll.txt", "r")
votes = polls.read().split(", ")
yea = votes.count("yea")
nay = votes.count("nay")
print("Yeas: " , yea)
print("Nays: " , nay)
polls.close()
