#1. Given a list of numbers, write code to iterate through the list and calculate the sum of all even numbers. Print the resulting sum.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evensum = 0
for num in numbers:
    if num % 2 == 0: # makes sure to only use even numbers, if odd num % 2 would = 1.
        evensum += num
print(evensum) # adds 2 + 4 + 6 + 8 + 10 = 30
print() #add space between each problem

#2. With a list of strings provided, write code that counts how many times the word "Olympic" appears in the list, and then print the count.

words = ["Rangers", "Olympic", "Ranier", "Washington", "Seattle", "Olympic", "College", "Navy" ]
Olympic_count = words.count("Olympic")
print("Amount of times that 'Olympic' appears:", Olympic_count)
print() #add space between each problem

#3. Given a list of strings, write code to create a new list that includes only the strings longer than three characters.
#Print the resulting filtered list.

list = ["the", "coffee", "is", "in", "the", "cabinet", "in", "our", "kitchen"]
for longerword in list:
    if len(longerword) > 3:
        print(longerword)
print() #add space between each problem

#4. For a list of integers, write code that counts how many numbers are positive and how many are negative, then print both counts.

integers = [13, -42, 18, 90, 82, 27, -43, -7, 83, 98, -12]
pos_counter = 0 
neg_counter = 0
for number in integers:
    if number >= 0:
        pos_counter += 1 # increment of +1 for each positive number
    else: neg_counter += 1 # increment of +1 for each negative number
print(pos_counter)
print(neg_counter)
print() #add space between each problem

#5. For a list of integers, use a loop to build a new list where each element is the square of the corresponding element in the original list.
#Print the new list.

ints = [4, 3, 12, 1, 7, 6, 15, 10, 9, 11]
squared_ints = []
for int in ints:
    squared_ints.append(int ** 2) # append takes values from ints and stores the new values in squared_ints list
print(squared_ints)
