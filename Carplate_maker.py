#In plates.py, implement a program that prompts the user for a vanity plate
# then output Valid if meets all of the requirements or Invalid if it does not.
#Assume that any letters in the user’s input will be uppercase.
#Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not.
#Assume that s will be a str.
#You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).

#requirements for vanity plates:
#“All vanity plates must start with at least two letters.”
#“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
#“Numbers cannot be used in the middle of a plate; they must come at the end, & first number used cannot be a ‘0’.”
#“No periods, spaces, or punctuation marks are allowed.”


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    #1 = Must start with 2 letters:
    if not plate[0].isalpha() or not plate[1].isalpha():
        return False
 #2 = max 6 and min 2 characters:
    if len(plate) < 2 or len(plate) > 6:
        return False
#3 = numbers must come at the end of the plate:
#checks if the license plate ends with one or two digits
#If any of the conditions is true, the function continues to check if there are any digits in the middle of the plate.
    if plate[-2:].isdigit() or plate[-1:].isdigit() or plate[-3:].isdigit():
       # Check that there are no digits in the middle of the plate:
       #The for loop checks each character in the middle of the plate
       # starts from 3rd character (= index 2) and ending 2 characters before the end of the plate (=index len(plate) - 3))
       #we know that the last two or one characters of the plate are digits, so we don't need to check those
       #If character being checked is a digit: function immediately returns False --> indicates digits in middle of plate
       #If loop completes without finding any digits in the middle of the plate: valid according license plate
        for i in range(2, len(plate)-3):
            if plate[i].isdigit():
                return False
        #4 = Check for periods, spaces, and punctuation marks:
        if '.' in plate or ' ' in plate or any(c for c in plate if c.isalnum() == False):
            return False
        return True
    # 5. Check for license plates consisting only of letters
    if plate.isalpha():
        return True

    else:
        return False
main()

