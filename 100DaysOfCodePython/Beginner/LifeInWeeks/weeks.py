if __name__ == '__main__':
    print("This app calculates how many days, weeks and months you have left if you live until 90 years old YOLO")
    years_left = 90 - int(input("Enter your age: "))
    print(f"You have {years_left*365} days, {years_left*52} weeks and {years_left*12} months left.")


