# then outputs the number of calories in one portion of that fruit,
# (per the FDA’s poster for fruits, which is also available as text)
# Capitalization aside, assume that users will input fruits exactly as written in the poster (e.g., strawberries, not strawberry).
# Ignore any input that isn’t a fruit.

# Create a dictionary to store fruit names as keys and their corresponding calories as values

# Assignment
def main():
    # fruit names = keys, calories = values
    fruit_calories = {
        'apple': 130,
        'banana': 105,
        'orange': 62,
        'grapes': 69,
        'strawberries': 32,
        'watermelon': 46,
        'blueberries': 57,
        'kiwifruit': 90,
        'mango': 202,
        'pineapple': 82,
        'peach': 39,
        'sweet cherries': 100,
        'grapefruit': 52,
        'papaya': 119,
        'pomegranate': 234,
        'lemon': 24,
        'lime': 30,
        'avocado': 234,
        'coconut': 354,
        'figs': 107,
        'pear': 100

    }

    fruit = input("Fruit: ").lower() # input --> lowercase
    if fruit in fruit_calories: # Check if the entered fruit matches item in dictionary
        print("Calories:", fruit_calories[fruit])
    else:
        pass # error message

main()