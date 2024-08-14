#implement a program that prompts the user to insert a coin, one at a time,
#each time informing the user of the amount due.
#Once the user has inputted at least 50 cents, output how many cents in change the user is owed.
# Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

def main():
    accepted_coins = [5, 10, 25] # Accepted coin denominations
    amount = 0
    while True:
        if amount < 50:
            coin = int(input("Insert Coin: "))
            amount += coin
            print("Amount Due:",  50 - amount)
            continue
        elif amount == 50:
            print("Change Owed: 0")
            break
        elif amount > 50:
            change = amount - 50
            print(f"Change Owed: {change}")
            break

if __name__ == '__main__':
    main()