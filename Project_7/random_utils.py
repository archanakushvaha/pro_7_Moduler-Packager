import random


def random_number():
    return random.randint(1, 100)


def dataset_sampling(data, count):
    if count > len(data):
        return "Count is greater than dataset size"

    return random.sample(data, count)


def game_simulation():
    user = input("Enter your choice (1-6): ")

    if not user.isdigit() or not 1 <= int(user) <= 6:
        print("Please enter a number from 1 to 6")
        return

    user = int(user)
    computer = random.randint(1, 6)

    print("Computer choice:", computer)

    if user == computer:
        print("You Win!")
    else:
        print("You Lose!")
