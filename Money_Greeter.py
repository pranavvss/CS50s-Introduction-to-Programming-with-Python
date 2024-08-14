#prompts the user for a greeting.
#If the greeting starts with “hello”, output $0.
#If the greeting starts with an “h” (but not “hello”), output $20.
#Otherwise, output $100.
#Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

def main():
    # Prompt user for greeting
    greeting = input("Hi:").lower().strip()
    if "hello" in greeting:
        return "$0"
    elif greeting.startswith("h"):
        return "$20"
    else:
        return "$100"
print(main())