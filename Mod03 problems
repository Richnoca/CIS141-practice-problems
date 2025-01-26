#Module 3 practice problems

# 1. Prompt the user for a word. Then, prompt the user for how many times they'd like that word repeated.
#Use the skills you learned in this module to print the word the correct number of times.

word = input("Can you choose a word for me?")
number = int(input("now how many times do you want to repeat that word?"))
print((word + " ") * number)
print("")

#2. Prompt the user for their name and their age. Calculate their age next year. 
#Use string concatenation to print "Hello, <name>! You are <age1> years old. Next year, you will be <age2> years old."

name = input("What is your name?")
age1 = int(input("Hi, " + name + ", How old are you?"))
age2 = age1 + 1
print("Hello, " + name + "! you are " + str(age1) + " years old. Next year, you will be " + str(age2) + " years old.")
print("")

#3. Prompt the user for a sentence and a word to try to find in that sentence. 
#Have the program print out whether the word was found in the sentence. (i.e. True or False)

sentence = input("Can you write any sentence in the world for me?")
chosenword = input("Now can you write a word that may or may not be in that sentence?")
print(chosenword in sentence)
print("")

#4. Prompt the user for: a word, a first index, and a last index. 
#Slice the word at the indexes provided by the user and print to the screen.

word4 = input("Can you choose a preferably long word for me?")
index1 = int(input("Okay now choose a first index."))
index2 = int(input("Now pick a final index for me please."))
sliced = word4[index1:index2]
print("when I slice your word, it now reads as" , sliced, ".")
print("")

#5. Print 3 words with a | character (called a pipe) in between them. 
#Use the appropriate keyword argument in print() to do so.

firstword = input("Can you choose the first of 3 words for me?")
secondword = input("Now input the second please.")
thirdword = input("And finally the third word.")
blank = "" #Using this so there is a bar behind the third word
print("Okay, the words you chose were:" , firstword , "," , secondword, ", and" , thirdword, ".")
print("And here is them seperated by pipes:" ,firstword, secondword, thirdword, blank, sep="|")
