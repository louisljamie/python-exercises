# 1 Conditional Basics

    # a prompt the user for a day of the week, print out whether the day is Monday or not

what_day = input("What day of the week is it? ")
if what_day.lower() == "monday":
    print("It's Monday!")
else:
    print("It's not Monday")



    # b prompt the user for a day of the week, print out whether the day is a weekday or a weekend
    
what_day = input("What day of the week is it? ")
if what_day.lower() == "saturday" or what_day.lower() == "sunday":
    print("It's the weekend!")
else:
    print("It is" what_day.capitalize(), ",a weekday, so sorry")


    # c create variables and make up values for:
        # - the number of hours worked in one week
        # - the hourly rate
        # - how much the week's paycheck will be
        # write the python code that calculates the weekly paycheck. 
        # You get paid time and a half if you work more than 40 hours

hours_worked = input("How many hours did you work this week?: ")
hours_worked = int(hours_worked)
hourly_rate = 15
week_pay = hours_worked * hourly_rate
overtime = (hours_worked - 40) * (hourly_rate * 1.5)
weekly_paycheck = hours_worked * hourly_rate
if hours_worked >= 40:
    print("Your weekly paycheck is $", weekly_paycheck + overtime, "it includes $", overtime, "in overtime pay")
else:
    print("Your weekly paycheck is $", weekly_paycheck)
    
    

# Loop Basics

    # a While
        # - Create an integer variable i with a value of 5.
i  =  5
        
        # - Create a while loop that runs so long as i is less than or equal to 15
        
while i <= 15:
   
            
        # - Each loop iteration, output the current value of i, then increment i by one. 
i=5
while i <= 15:
    print (i)
    i += 1
    
    
        # - Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.     

llist1 = range(1,100)
num = 0

while(num < len(list1)):
    if list1[num] % 2 == 0:
        print(list1[num], end=" ")
    num += 1

            
        # - Alter your loop to count backwards by 5's from 100 to -10.
for i in range(100,-10, 5):
    print(i)


i = 100

while i >= -10:
    print(i)
    i -= 5

        # - Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:

i = 2
x = 1000000
while i < x:
    print(i)
    i = i ** 2

#    i = 2
#
#    while i < 1_000_000:
#        print(i)
#        i**=2

        # - Write a loop that uses print to create the output shown below.
        
for i in range(100, 5, 5):
    while i >= 5:
     print(i)
    
        
    # b For Loops
        # - Write some code that prompts the user for a number, then shows a multiplication table 
        # up through 10 for that number.
         # - For example, if the user enters 7, your program should output:

int = input("Enter a number: ")
int = int(int)
for i in range(1,11):
    print("Multiplication Table for", int, '':" \n ", "x", i, "=", int * i)




for i in range(1, 11):
    print(f'{user_num} x {i} = {int(user_num) * i}')
# - Create a for loop that uses print to create the output shown below.

        
for i in range(1,10):
    print(str(i) * i)
    

    # c break and continue
        # Write a program that prompts the user for a positive integer. Next write a loop that prints 
        # out the numbers from the number the user entered down to 1.
        
int = input("Enter a positive integer: ")
int = int(int)
for i in range(int, 0, -1):
    print(i)
------------------

while True:
    user_num = input('Please enter a positive number: ')

    if user_num.isdigit() == True:
        print('This is a digit')
            if int(user_num) > 0:
                print('The number is positive!')
                break

user_num = int(user_num)
for i in range(user_num, 0, -1):
    print(i)

        # The input function can be used to prompt for input and use that input in your python code. Prompt 
        # the user to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user 
        # entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)

# int = input("Enter a positive integer: ")
# int = int(int)
# for i in range(0, int + 1):
#    print(i)


while True:
    user_num = input('Please enter a positive number: ')

        if user_num.isdigit() == True:
            print('This is a digit')
            if int(user_num) > 0:
                print('The number is positive!')
                break

for i in range(int(user_num)+1):
    print(i)


        # Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if 
        # they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the 
        # odd numbers between 1 and 50, except for the number the user entered.
        
# int = input("Enter an odd number between 1 and 50: ")
# int = int(int)
# for i in range(1, 50, 2):
#    if i == int:
#        print("Yikes! Skipping number:", int)
#        continue
#    print("Here is an odd number:", i)


while True:
    user_num = input('Enter an odd number between 1 and 50: ')

    if user_num.isdigit():
        print('This is a digit')
        if int(user_num) % 2 != 0:
            print('This is an odd number')
            if (int(user_num) > 1) and (int(user_num) < 50):
                print('This number is between 1 and 50')
                break

user_num = int(user_num)

for i in range(1,50):
    if i == user_num:
        print('We skipped this!')
        continue
    if i % 2 == 1:
        print(i)


        

# 3 Fizzbuzz
# One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.
        # Write a program that prints the numbers from 1 to 100.
        # For multiples of three print "Fizz" instead of the number
        # For the multiples of five print "Buzz".
        # For numbers which are multiples of both three and five print "FizzBuzz".

for i in range(1,101):
    if i % 15 == 0:
        print('FizzBuzz')
        continue
    if i % 3 == 0:
        print('Fizz')
        continue
    if i % 5 == 0:
        print('Buzz')
        continue
    print(i)
        




        
# 4 Display a table of powers.
        # Prompt the user to enter an integer.
        # Display a table of squares and cubes from 1 to the value entered.
        # Ask if the user wants to continue.
        # Assume that the user will enter valid data.
        # Only continue if the user agrees to.
        # Research python's format string specifiers to align the table



user_num = int(input('Enter an ineger: '))

user_num, user_num**2, user_num**3

while True:
    user_num = int(input('Enter an ineger: '))

    for i in range(1, user_num+1):
        print(f'{i}  |{i**2}  |{i**3}')

    user_yn = input('Would you like to continue? (y/n): ')
    if user_yn.lower() !='y':
        break


# 5 Convert given number grades into letter grades.
            # Prompt the user for a numerical grade from 0 to 100.
            # Display the corresponding letter grade.
            # Prompt the user to continue.
            # Assume that the user will enter valid integers for the grades.
            # The application should only continue if the user agrees to.
            # Grade Ranges:
                # A : 100 - 88
                # B : 87 - 80
                # C : 79 - 67
                # D : 66 - 60
                # F : 59 - 0

user_grade = int(input('Enter a numerical grade from 0-100: '))

if user_grade >= 88:
    print('A')
elif user_grade >= 80:
    print('B')
elif user_grade >= 67:
    print('C')
elif user_grade >= 60:
    print('D')
else:
    print('F')


# Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+)

while True:
    user_grade = int(input('Enter a numerical grade from 0-100: '))

    if user_grade >= 88:
        print('A')
    elif user_grade >= 80:
        print('B')
    elif user_grade >= 67:
        print('C')
    elif user_grade >= 60:
        print('D')
    else:
        print('F')

    user_yn = input('Would you like to continue? (y/n)')
    if user_yn.lower() != 'y':
        break


# 6 Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.
    # Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.


    books = [{'title': 'title111', 'author': 'author1', 'genre': 'genre1'},
             {'title': 'title222', 'author': 'author1', 'genre': 'genre2'},
             {'title': 'title333', 'author': 'author2', 'genre': 'genre2'},
             {'title': 'title444', 'author': 'author3', 'genre': 'genre2'}]

for book in books:
    print(book)

user_genre = input('Enter a genre: ')

for book in books:
    if book['genre'] == user_genre:
        book['title']

books