# Import and test 3 of the functions from your functions exercise file. Import each function in a different way:

    # a Run an interactive python session and import the module. Call the is_vowel function using the . syntax.
    # b Create a file named import_exericses.py. Within this file, use from to import the calculate_tip function directly. Call this function with values you choose and print the result.
    # c Create a jupyter notebook named import_exercises.ipynb. Use from to import the get_letter_grade function and give it an alias. Test this function in your notebook.
        # Make sure your code that tests the function imports is run from the same directory that your functions exercise file is in.



from functions_exercises import calculate_tip

calculate_tip()



# Read about and use the itertools module from the python standard library to help you solve the following problems:
    # How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
    # How many different combinations are there of 2 letters from "abcd"?
    # How many different permutations are there of 2 letters from "abcd"?   cd


list(itertools.product('abc', [1,2,3]))

len(list(itertools.combinations('abcd', 2)))

len(list(itertools.permutations('abcd', 2)))





# Save this file as profiles.json inside of your exercises directory (right click -> save file as...).
    # Use the load function from the json module to open this file.

        # import json
        # json.load(open('profiles.json'))
# Your code should produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information:
    # Total number of users
    # Number of active users
    # Number of inactive users
    # Grand total of balances for all users
    # Average balance per user
    # User with the lowest balance
    # User with the highest balance
    # Most common favorite fruit
    # Least most common favorite fruit
    # Total number of unread messages for all users