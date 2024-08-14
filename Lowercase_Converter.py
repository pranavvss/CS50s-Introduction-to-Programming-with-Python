#Objective of the code is to turn mixed case words into all lowercase (from camelcase to snakecase)
# Error check: use a while loop to prompt the user for input
# only perform the code when a valid camel case variable name is provided.

# Checks:
# Input not empty
# 1st character of input in lowercase
# input is a valid identifier and allowed as a Python variable name.
# If conditions fulfilled = carry out code
# If conditions not fulfilled = error message

# THIS IS THE 2ND LOOP --> Converts camel case string to snake case => camel case = input from user
# loop processes each letter in camel_case string INDIVIDUALLY
# then builds the snake_case string letter by letter

def camel_to_snake(camel_case):
    print("This program prints your input in complete lowercase")
    snake_case = '' # initialise empty string variable to store converted version of variable

    for letter in camel_case:
        if letter.islower():
            snake_case += letter # lowercase letter character is directly appended to the snake_case string
        else:
            snake_case += '_' + letter.lower() #. If uppercase letter -> add underscore (_) then lowercase letter to snake_case string,
    return snake_case

# THIS IS THE '1st' LOOP --> Prompt user for the variable name in camel case
while True:

    camel_var = input("Enter your message in camelcase please. Message must start in lowercase: ")
    if not camel_var: # checks for empty input from the user
        print("Your input is empty. Please repeat your message in the correct format.")
    elif not camel_var[0].islower(): # checks for the status of the 1st letter of the input
        print("The variable name must start with a lowercase letter. Please repeat your message in the correct format.")
    elif not camel_var.isidentifier(): # checks if the string is a valid identifier according to Python's naming rules
        print("This variable name is invalid. Please repeat your message in the correct format.")
    else:
        break # terminates the while loop if all conditions are met

# Convert camel case to snake case
snake_var = camel_to_snake(camel_var)

# Output the snake case variable name
print("Thank you for your input. Your variable name in snake case is:", snake_var)



