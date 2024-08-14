#implement a program that enables a user to place an order, prompting them for items, one per line,
# until the user inputs control-d (which is a common way of ending one’s input to a program).
# #After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($)
# #and formatted to two decimal places.
# #Treat the user’s input case insensitively.
# #Ignore any input that isn’t an item. Assume that every item on the menu will be titlecased
#You might want to print a new line so that the user’s cursor (and subsequent prompt) doesn’t remain on the same line as your program’s own prompt.
#Inputting control-d does not require inputting Enter as well, and so the user’s cursor (and subsequent prompt)
#might thus remain on the same line as your program’s own prompt. You can move the user’s cursor to a new line by printing \n yourself!


def main():
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    order = []
    while True:
        try:
            items = input("Item:\n ").lower().title()
            if items in menu:
                order.append(items)
                total = 0
                for item in order:
                     total += menu[item]
                     #loops through each item in the order list
                     # then adds the corresponding price from the menu dictionary to the total variable.
            print(f"${total:.2f}") # for 2 d.p.
        except EOFError:
            break

if __name__ == '__main__':
    main()