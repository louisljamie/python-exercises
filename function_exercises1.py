# Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

from webbrowser import get


#user_input = input('Enter 2: ')



def is_two(x):

    if x == 2 or x == '2':
        return True
    else:
        return False
    
# is_two(user_input)


# Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

# user_input = input('Enter a letter from A-Z: ')

def is_vowel(letter):
    if letter.lower() in 'aeiou':
        return True
    else:
        return False

# is_vowel(user_input)

# check if theinput is a certain type
# if type(somethoing) == str:
#    return True
# else:
#    return False

# Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

# user_input = input('Enter a letter from A-Z: ')

def is_consonant(x):
    if x.lower() in 'bcdfghjklmnpqrstvwxyz':
        return True
    else:
        return False

# is_consonant(user_input)

# Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.


# user_input = input('Enter a word: ')

def cap_first_consonant(x):
    if is_consonant(x) in 'bcdfghjklmnpqrstvwxyz':
        return x.capitalize()
    else:
        return x
    
# cap_first_consonant(user_input)

def is_consonant(x):
    if type(x) == str:
        if len (x) == 1 and x.isalpha():
            return (not is_vowel(x))
        else:
            return False
    else:
        return False
           

# Define a function named calculate_tip for tip calculation. ask for the bill total. ask for the percentage of the tip . return the amount to tip.

def calculate_tip (bill, tip, split):
    bill = float(input('Enter the bill total...": '))
    tip = float(input('Enter the tip percentage: '))
    split = float(input('Enter the amount of people spliting the bill: '))
    x = (bill + (0.1 * tip)) / split
    return ("Each person have to pay $", x, "amount")

# calculate_tip()

# Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

def apply_discount(x, y):
    return x - (x * y)

# apply_discount()
# Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

def handle_commas(x):
    return int(x.replace(',', ''))



# Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).


#user_input = input('Enter a number grade: ')

def get_letter_grade(x):
    if x >= 88:
        return 'A'
    elif x >= 80:
        return 'B'
    elif x >= 67:
        return 'C'
    elif x >= 60:
        return 'D'
    else:
        return 'F'
    
# get_letter_grade(user_input)

# Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(x):
    return x.translate({ord(i): None for i in 'aeiouAEIOU'})


# Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
    # leading and trailing whitespace should be removed
        # everything should be lowercase
            # spaces should be replaced with underscores
                # for example:
                # Name will become name
                # First Name will become first_name
                # % Completed will become completed
                
def normalize_name(x):
    return x.strip().lower().replace(' ', '_').translate({ord(i): None for i in '!@#$%^&*()[]{};:,./<>?\|`~-=_+'})


# Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]
# Additional Exercise

def cumulative_sum(x):
    return [sum(x[:i+1]) for i in range(len(x))]


# Once you've completed the above exercises, follow the directions from https://gist.github.com/zgulde/ec8ed80ad8216905cda83d5645c60886 in order to thouroughly comment your code to explain your code.
# Bonus
# Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.
# Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
# col_index('A') returns 1
# col_index('B') returns 2
# col_index('AA') returns 27
