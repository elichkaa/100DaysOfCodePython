if __name__ == '__main__':
    print("This app checks if a given year is a leap year.")
    year = int(input("Enter year to check: "))
    is_leap = False
    if year % 4 == 0:
        if year % 100 != 0:
            is_leap = True
        else:
            if year % 400 == 0:
                is_leap = True
    if is_leap:
        print(f"Yes, {year} is a leap year.")
    else:
        print(f"No, {year} is not a leap year.")