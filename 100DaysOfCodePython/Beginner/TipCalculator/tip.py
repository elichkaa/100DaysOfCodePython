if __name__ == '__main__':
    print("Welcome to the tip calculator.")
    bill = float(input("What was the total bill? $"))
    tip = int(input("What percentage tip would you like to give? "))
    people = int(input("How many people to split the bill? "))
    bill_per_person = (bill + 0.01*tip*bill)/people
    print(f"Each person should pay: ${round(bill_per_person, 2)}")
