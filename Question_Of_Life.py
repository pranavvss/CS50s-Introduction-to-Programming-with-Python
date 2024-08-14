#implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything,
#outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. O
#therwise output No.

def main():
    number = input("What is the answer to life?").lower()
    if number in ['42', 'forty two', 'forty-two']:
        return "Yes"
    else:
        return "No"

print(main())