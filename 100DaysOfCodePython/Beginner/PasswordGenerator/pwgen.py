import random
import string

if __name__ == '__main__':
    print("Welcome to the Python Password Generator!")
    nr_letters = int(input("How many letters would you like in your password?: "))
    nr_symbols = int(input(f"How many symbols would you like?: "))
    nr_numbers = int(input(f"How many numbers would you like?: "))

    accepted_symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    letters = ''.join(random.choice(string.ascii_letters) for i in range(nr_letters))
    symbols = ''.join(random.choice(accepted_symbols) for i in range(nr_symbols))
    numbers = ''.join(random.choice(string.digits) for i in range(nr_numbers))
    together = list(numbers + symbols + letters)
    random.shuffle(together)
    pw = ''.join(together)
    print(f"Here is your password: {pw}")
