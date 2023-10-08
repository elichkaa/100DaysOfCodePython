prompt = "Guess letter: "
success = "You are one step closer to the rescue. Well done and continue in the same spirit so you don't die."
blank = '_'


def repeating(letter):
    return f"You have already guessed {letter}. Try again."


def fail(letter):
    return f"Letter {letter} is not contained in word. Another one of your limbs is at risk. Try again or die."


def progress(blanks):
    return f"Progress so far: {''.join(blanks)}"


def endgame(word, won):
    if won:
        return f"Congratulations! You guessed the word {word} and earned the right to keep on living."
    else:
        return (f"You didn't guess the word {word} correctly and have therefore been executed. "
                f"Better luck in your next life.")
