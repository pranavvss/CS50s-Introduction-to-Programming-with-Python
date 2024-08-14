
# Prompt the user for input
message = input("Enter text: ")

# Define function to remove vowels from info entered by user
def shorten(message):
    vowels = "AEIOUaeiou" # string of vowels defined
    result = " " # empty string is initialised to store the result

    # Iterate for each letter in the text entered
    for char in message:
        # Check if the character is not a vowel
        if char not in vowels:
            result += char # only adding the non vowels to the result string

    return result

# Call  function and store the result
result = shorten(message)

# Print the result
print(result)