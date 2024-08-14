import random

def get_level():
    while True:
        level = input("Level: ")
        if level in ["1", "2", "3"]:
            return int(level)
        else:
            continue

def generate_integer(level):
    problems = []
    for _ in range(10):
        x = random.randint(0, 9) if level == 1 else random.randint(10**(level-1), 10**level-1)
        y = random.randint(0, 9) if level == 1 else random.randint(10**(level-1), 10**level-1)
        problem = f"{x} + {y} = "
        answer = x + y
        problems.append((problem, answer))
    return problems

def main():
    level = get_level()
    problems = generate_integer(level)
    score = 0
    for problem, answer in problems:
        print(problem)
        num_tries = 0
        while num_tries < 3:
            user_answer = input("Answer: ")
            if user_answer.isdigit():
                user_answer = int(user_answer)
                if user_answer == answer:
                    print("Correct!")
                    score += 1
                    break
                else:
                    num_tries += 1
                    print("Incorrect answer. Try again.")
            else:
                num_tries += 1
                print("Incorrect answer. Try again.")
        if num_tries >= 3:
            print(f"The correct answer is: {answer}")

    print(f"{score}/10")

if __name__ == "__main__":
    main()
