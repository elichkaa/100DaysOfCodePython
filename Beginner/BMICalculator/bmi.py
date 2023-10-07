if __name__ == '__main__':
    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in m: "))
    bmi = weight / height ** 2
    category = ""
    if bmi < 16:
        category = "severely thin"
    elif bmi < 17:
        category = "moderately thin"
    elif bmi < 18.5:
        category = "mildly thin"
    elif bmi < 25:
        category = "normal"
    elif bmi < 30:
        category = "pre-obese"
    elif bmi < 35:
        category = "obese class I"
    elif bmi < 40:
        category = "obese class II"
    else:
        category = "obese class III"

    print(f"Your BMI is {round(bmi, 2)} and you categorize as {category}")