import art
import data
import random


if __name__ == '__main__':
    print(art.logo)
    choice_correct = True
    score = 0
    first = random.choice(data.data)
    while choice_correct:
        second = random.choice(data.data)
        print(f"Compare A: {first['name']}, {first['description']}, from {first['country']}")
        print(art.vs)
        while second == first:
            second = random.choice(data.data)
        print(f"Compare B: {second['name']}, {second['description']}, from {second['country']}")
        choice = input("Who has more followers? Type 'A' or 'B': ")
        if choice == 'A':
            if first['follower_count'] < second['follower_count']:
                choice_correct = False
            else:
                score += 1
        elif choice == 'B':
            first = second
            if first['follower_count'] > second['follower_count']:
                choice_correct = False
            else:
                score += 1
        else:
            print("Invalid choice")
        if not choice_correct:
            print(f"Game over! Your score is {score}")
        else:
            print(f"Correct! Your score has increased: {score}")
