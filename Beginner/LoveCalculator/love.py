if __name__ == '__main__':
    print("This app will calculate what is the love compatibility between you and your crush just based on your names!")
    first_name = input("Enter name of first person: ")
    second_name = input("Enter name of second person: ")
    combined = (first_name + second_name).lower()
    # It works by counting the occurrences of the word true love in both the names
    t = combined.count("t")
    r = combined.count("r")
    u = combined.count("u")
    e = combined.count("e")
    l = combined.count("l")
    o = combined.count("o")
    v = combined.count("v")
    score = int(str(t + r + u + e) + str(l + o + v + e))
    print(f"Your score: {score}")
    if (score < 10) or (score > 90):
        print("You go together like coke and mentos.")
    elif (score >= 40) or (score <= 50):
        print("You are alright together.")
    else:
        print("No comment ^^")
