'''
#1. Write a function called count_vowels(input) that takes a string
    and returns the number of vowels (a, e, i, o, u) in it.
    Test: Olympic College Rangers (7 vowels)
    Input: string (input)
    output: int
    function: for function that checks each character, adds 1 if character is vowels
'''
def count_vowels(input):
    counter = 0
    vowels = "aeiouAEIOU"
    for char in input:
        if char in vowels:
            counter += 1
    return counter

num_vowels = count_vowels("Olympic College Rangers")
print("there are" , num_vowels , "vowels in Olympic College Rangers.")

print()
'''
#2. Write a function called is_palindrome(s) that checks whether a string is a palindrome
    (reads the same forward and backward, ignoring case). The function should returns
    either True or False.
    Test: racecar (True), pikachu (False), Racecar (true)
    Input: string (s)
    Output: boolean
    Function: lowercase str, flip str and save to new vari (flipped_str) and then compare str and flipped_str
'''
def is_palindrome(s):
    lower_s = s.lower()
    flipped_s= lower_s[::-1]
    return lower_s == flipped_s

# Tests
print(is_palindrome("racecar"))
print(is_palindrome("pikachu"))
print(is_palindrome("Racecar"))

print()
'''
#3. In the game Pokemon, certain types of Pokemon do extra damage to other types.
    For example, water is very effective to fight fire.
    Write a function called type_advantage(attacker, defender) that takes two Pokémon types as
    strings and returns "Super Effective", "Not Very Effective", or "Neutral" based on
    simple type effectiveness rules. Your solution only needs to work for these three sets of input:
    print(type_advantage("Water", "Fire"))  # "Super Effective"
    print(type_advantage("Fire", "Water"))  # "Not Very Effective"
    print(type_advantage("Electric", "Grass"))  # "Neutral"
    Test: each type and its effectiveness
    Input: string
    Output: string
    Function: simple if/elif statements while using the and operator to check both variables to be true
'''

def type_advantage(attacker, defender):
    if attacker == "Water" and defender == "Fire":
        return "Super Effective"
    elif attacker == "Fire" and defender == "Water":
        return "Not Very Effective"
    elif attacker == "Electric" and defender == "Grass":
        return "Neutral"
    else:
        return "Neutral"

# Tests
print(type_advantage("Water", "Fire"))  # "Super Effective"
print(type_advantage("Fire", "Water"))  # "Not Very Effective"
print(type_advantage("Electric", "Grass"))  # "Neutral"

print()
'''
#4. Write a function called ferry_fare(age, vehicle) that calculates the Washington State Ferry fare
    based on age and whether the person has a vehicle. Assume the following rates:
    * Adults (19-64): $10 without a vehicle, $20 with a vehicle.
    * Seniors (65+): $5 without a vehicle, $15 with a vehicle.
    * Children (0-18): Free.
    Test: cost for ferry ticket by age and vehicle
    Input: int and boolean
    Output: int (dollar cost)
    Function: dollar cost for each ticket
'''

def ferry_fare(age, vehicle):
    if age <= 18:
        return 0

    elif age <= 64:
        if vehicle:
            return 20
        else:
            return 10

    elif age >= 65:
        if vehicle:
            return 15
        else:
            return 5

print(ferry_fare(10, True))  # 0
print(ferry_fare(25, True))  # 20
print(ferry_fare(25, False))  # 10
print(ferry_fare(70, True))  # 15
print(ferry_fare(70, False))  # 5
print()

'''
#5. Write a function called level_up(experience) that takes a player's experience points
    and returns their new level based on these rules:
    * 0-99 XP → Level 1
    * 100-199 XP → Level 2
    * 200+ XP → Level 3
    Test: experience for each level
    Input: int that returns a string
    Output: str
    Function: if elif statements that return a level based on the XP being printed
'''
def level_up(experience):
    if experience <= 99:
        return "Level 1"
    
    elif experience <= 199:
        return "Level 2"
    
    elif experience >= 200:
        return "Level 3"

print("You are currently " + level_up(27))
print("You are currently " + level_up(124))
print("You are currently " + level_up(773))
