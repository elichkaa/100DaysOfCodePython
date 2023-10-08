import random

if __name__ == '__main__':
    # Chooses a random name out of a list of names and the picked out person has to pay the bill
    names = input("Give me everybody's names, separated by comma and space: ").split(", ")
    chosenIndex = random.randint(0, len(names) - 1)
    # Alternatively you can use random.choice(names) and its gonna pick out an element for you
    print(f"{names[chosenIndex]} is going to buy the meal today!")
    print(f"{random.choice(names)} is going to buy the meal today!")
