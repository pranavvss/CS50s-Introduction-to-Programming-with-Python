#implement a program that:
#Expects zero or two command-line arguments:
#Zero if the user would like to output text in a random font.
#Two if the user would like to output text in a specific font, in which case:
# the first of the two should be -f or --font, and the second of the two should be the name of the font.
#Prompts the user for a str of text.
#Outputs that text in the desired font.
#If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font,
#the program should exit via sys.exit with an error message.

import pyfiglet
import sys

def main(font):
    if len(sys.argv) == 1:
        font = pyfiglet.Figlet(font='random')
    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
        try:
            font = pyfiglet.Figlet(font=sys.argv[2])
        except pyfiglet.FontNotFound:
            sys.exit(f"Error: The font '{sys.argv[2]}' has not been found.")
    else:
        sys.exit("Error: Invalid command-line arguments.")

    return font

if __name__ == '__main__':
    font = None
    font = main(font)
    text = input("Enter text to display: ")
    print(font.renderText(text))

#checks whether the script is being run as the main program or being imported as a module into another program.
    #When a Python module is imported, Python sets the special variable __name__ to the name of the module.
    # However, when a Python script is run as the main program, Python sets the __name__ variable to the string '__main__'.
    # Therefore, the if __name__ == '__main__': block is executed only when the script is being run as the main program.
    # This allows you to define code that should be executed only when the script is run as the main program, and not when it is imported as a module.

# font variable is initialized to None,then the main() function is called with the font variable as an argument.
# The return value of main() is then assigned to font.
# After that, the user is prompted to enter some text to display, and the renderText() method of the font object is used to render the text in the desired font.
#  Finally, the rendered text is printed to the console using the print() function.
#1 initializing the font variable,
# getting input from the user,
# rendering and displaying the text in the desired font.