# 1. Create a program that prints the following output to the screen: "Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked."

print("Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked.")


# 2. Create a program that prompts for 2 numbers and then outputs the addition, subtraction, multiplication, and division of the first number by the second number.

print("")
user_name = input("What is your name?")
print("Hello," , user_name)
import math
x = int(input("Can you pick a number for me?"))
y = int(input("Okay that's a good number, can you give me one more?"))
print("")
print("Okay, I can do some basic arithmethic with those numbers!")
print("")
print("this is the value you can get if you add them together:" , (x+y))
print("")
print("this is the value you can get if you subtract the second number from the first:", (x-y))
print("")
print("this is the value you can get if you multiply them together:" , (x*y))
print("")
print("and lastly this is the value you would get if you divided your first number by the second:" , (x/y))
print("")
print("Thank you" , user_name , "for using me as your calculator!")
print("")


# 3. Create a program that prompts for the side lengths of a triangle and computes the area using Heron's formula. (https://en.wikipedia.org/wiki/Heron%27s_formula)

print("Okay," , user_name)
print("Next I'm going to solve Heron's Formula, with 3 new numbers that YOU give me.")
print("Heron's Formula gives you the area of a triangle if you know the length of the 3 sides and they are greater than 1.")

import math
a = int(input("What would you like the length of the first side to be?"))
b = int(input("and side b?"))
c = int(input("Then lastly what's the length side c?"))
semi = (a + b + c) / 2 #couldn't figure out how to compute all in one equation at first, so I solved for semiperimeter first
print("")
area = float(math.sqrt(semi*(semi - a)*(semi - b)*(semi - c)))
# took me 30 minutes to realize that I needed a '*' between each variable in the above equation
print("with those side lengths, the area of your triangle would be" , area)
print("")


# 4. Create a program that computes different statistics given five numbers including the total, average, minimum, maximum, range, and standard deviation (https://en.wikipedia.org/wiki/Standard_deviation).

print("Lastly," , user_name)

import math
a, b, c, d, e = map(int, input("can you give me 5 numbers seperated by a space?").split())
print("")
print("Okay, you entered:" , a, b, c, d, e,)
print("Here's some quick calculations I can do with those numbers.")
print("")
total = a + b + c + d + e
print("The total of the values that you entered is:" , total)
print("")
average = float((a + b + c + d + e) / 5)
print("The average of the values that you entered is:" , average)
print("")
min = min(a, b, c, d, e)
print("The minimum value that you entered is:" , min)
print("")
max = max(a, b, c, d, e)
print("The maximum value that you entered is:" , max)
print("")
range = (max - min)
print("The range of the values that you entered is:" , range)
print("")
standev = float(math.sqrt(((a - average)**2 + (b - average)**2 + (c - average)**2 + (d - average)**2 + (e - average)**2) / 4))
# I assume this is Sample standard deviation of (n-1) for the denominator and not population standard deviation where denom would be 5
print("The Standard Deviation of the values that you entered is:" , standev)
print("")
print("Have a good day!")

'''https://www.geeksforgeeks.org/taking-multiple-inputs-from-user-in-python/ citation for how I learned to use .split() and map(
This was really bothering me as I didn't want to have to ask for a value line by line, and thought it would be simpler for the user
to input all of the values at once'''
