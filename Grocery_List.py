def main():
    grocery_list = {}
    while True:
        try:
            item = input().strip().lower()
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1
        except EOFError:
            # Sort the dictionary by item name in ascending order and returns a list of tuples
            sorted_list = sorted(grocery_list.items())
            # Print the grocery list
            for item, count in sorted_list:
                print(f"{count} {item.upper()}")
            break

if __name__ == '__main__':
    main()