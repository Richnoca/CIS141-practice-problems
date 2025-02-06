# Mod5 practice problems

#1. Prompt the user for a positive integer n. Use a while loop to sum all the integers from 1 up to n. Print the final sum.

num = int(input("please enter any positive integer: "))
sum = 0
i = 1
while i <= num:
    sum += i
    i += 1
print(f"the sum of numbers from 1 to your number, {num}, is {sum}.")
print("")

#2. Define a string variable (e.g., my_string = "Olympic College").
#Use a for loop to print each character on its own line. Convert each character to uppercase before printing.

string = "Super Bowl"
for char in string:
    print(char.upper())
print("")

#3. Use a for loop and the range() function to print all even numbers from 2 to 20.

for i in range(2, 22, 2):
    print(i)
print("")

#4. Use nested for loops to create a simple multiplication table for numbers 1 through 5.
# Format your output so that each row corresponds to multiplying by a specific number.

print("5 x 5 multiplication table:")
for j in range(1 , 6):
    for k in range(1, 6):
        print(j * k , end="\t")
    print()
print("")

#5. Write a program that continuously asks the user to input a number.
# If the user enters 0, immediately stop asking for more numbers.
# Otherwise, print the number they entered. Sample interaction:

usernum = int(input("enter a number (0 to stop): "))
while usernum != 0:
    print("You entered: " , usernum)
    usernum = int(input("enter a number (0 to stop): "))
print("Exiting...")
