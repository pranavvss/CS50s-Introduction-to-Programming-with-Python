#implement a program that prompts the user for a str in English and then outputs the “emojized” version of that str,
#converting any codes (or aliases) therein to their corresponding emoji.
#Functions that need to be defined:
#main(), ask_user(), images(), alias(),

#STEP 0 = import library
import emoji

#STEP 1 = USER INPUT!
def ask_user():
    user_char = input("Enter your emoji command: ").strip()
    return user_char

#STEP 2 = CASE 1 emoji conversion
# Replace the colon delimiters with the corresponding emoji from the library
def images(user_char):
    emojized_char = emoji.emojize(user_char)
    return emojized_char

#STEP 3 = CASE 2 alias emoji conversion
# Iterate through the dictionary and replace any aliases with their corresponding emoji
def alias(user_input, emoji_aliases):
    for alias, emoji_char in emoji_aliases.items():
        user_input = user_input.replace(alias, emoji_char)
    return user_input

#Dictionary should be defined in main
#conditionals for what the ask_user function matches to run either images or alias
def main():
    emoji_aliases = {
        ":)": "😄",
        ":(": "😞",
        "<3": "❤️",
        ":D": "😃",
        ":P": "😛",
        ":O": "😮",
        ";)": "😉",
        ":/": "😕",
        ":|": "😐",
        ":3": "😻"
    }

    # Loop to ask for user input and output emojized version
while True:
        user_char = ask_user()
        if user_char.startswith(":") and user_char.endswith(":"):
            emojized_char = images(user_char)
        else:
            emojized_char = alias(user_char, emoji_aliases)
        print(emojized_char)
        break
main()
