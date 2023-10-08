import art
import messages
ALPHABET_SHIFT = 26


def encrypt(word):
    shift = int(input(messages.shift)) % ALPHABET_SHIFT
    for i in range(0, len(word)):
        if word[i] == ' ':
            continue
        val = ord(word[i])
        val += shift
        word[i] = chr(val)
    print(messages.result(''.join(word), True))


def decrypt(word):
    shift = int(input(messages.shift)) % ALPHABET_SHIFT
    for i in range(0, len(word)):
        if word[i] == ' ':
            continue
        val = ord(word[i])
        val -= shift
        word[i] = chr(val)
    print(messages.result(''.join(word), False))


if __name__ == '__main__':
    print(art.logo)
    end = False
    while not end:
        print(messages.prompt)
        choice = input()
        if choice == messages.encrypt:
            encrypt(list(input(messages.word)))
        elif choice == messages.decrypt:
            decrypt(list(input(messages.word)))
        else:
            print(messages.unavailable_command)
            continue
        print(messages.end)
        end_choice = input()
        if end_choice == messages.no:
            end = True
