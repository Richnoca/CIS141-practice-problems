# Cody Richnow Mod 4 practrice problems

# 1. Construct a truth table for the expression: (A AND B) OR (NOT B) where A and B each can be True or False. 
# variables: A and B
# rows: 2 possibility for A and 2 possibilities for B: 4 rows

# table columns + truth table: 
# A     B      (A AND B)    (NOT B)     (A AND B) OR (NOT B)
# T     T       T            F           T
# T     F       F            T           T
# F     T       F            F           F
# F     F       F            T           T

# 2. headlight sensor problems
sensor = int(input("enter a number 1-10 to determine if the headlights are on: "))
if sensor < 8: # wasnt sure if you wanted it as an input or not, but I thought it would make sense
    print("Headlights On")
else:
    print("Headlights off")
print("")

# 3. Prompt the user for their bank balance.
money = int(input("What is your bank balance? ")) # code is an issue if user inputs a dollar sign in their response
if money < 100: 
    print("False")
else:
    print("True")
print("")

# 4. A theater wants to enforce age restrictions for movie tickets.
age = int(input("Greetings, how old are you? "))
if age <= 13:
    print("You can see a G rated movie!")
elif age <= 17:
    print("You can see G and PG-13 rated movies!")
else:
    print("You can see all movies up to R rated!")
print("")

# 5.  A store charges $5 for shipping on any order under $50.
cost = int(input("what was the total cost of your order? "))
if cost < 50:
    print("With shipping, your cost is: $" , cost + 5)
else: 
    print("Your total cost is: $" , cost , ", shipping is on us!" )
