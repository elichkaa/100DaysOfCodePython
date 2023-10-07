import random


def determine_outcome(me, c):
    win = "You win"
    lose = "You lose"
    draw = "It's a draw"
    names = ["rock", "paper", "scissors"]
    if c == me:
        print(draw)
    elif len(names[me]) > len(names[c]) and abs(me - c) != 2:
        print(win)
    elif me == 0 and c == 2:
        print(win)
    else:
        print(lose)


if __name__ == '__main__':
    print("Welcome to Rock, Paper, Scissors!")
    ind = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. Your choice: "))
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''
    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''
    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
    rps = [rock, paper, scissors]
    print(rps[ind])
    comp = random.randint(0, 2)
    print(f"Computer chose: {rps[comp]}")
    determine_outcome(ind, comp)
