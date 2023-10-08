import random

import art
import words
import messages

if __name__ == '__main__':
    print(art.logo)
    word = random.choice(words.word_list)
    blanks = [messages.blank] * len(word)
    stage_counter = 6
    while stage_counter > 0 or messages.blank not in blanks:
        print(art.stages[stage_counter])
        letter = input(messages.prompt)
        if letter.lower() in blanks:
            print(messages.repeating(letter))
            continue
        if letter.lower() in word:
            for i in range(0, len(word)):
                if word[i] == letter:
                    blanks[i] = letter
            print(messages.success)
        else:
            stage_counter -= 1
            print(messages.fail(letter))
        print(messages.progress(blanks))
    if stage_counter == 0:
        print(art.stages[0])
        print(messages.endgame(word, False))
    else:
        print(messages.endgame(word, True))
