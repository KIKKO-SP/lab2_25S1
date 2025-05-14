def calculate_bmi(name, height, weight):
    bmi = weight / (height ** 2)
    rounded_bmi = round(bmi, 2)
    print(f"{name}, your BMI is: {rounded_bmi}")

    if bmi < 18.5:
        print(f"{name}, you are underweight.")
        return -1
    elif bmi < 25:
        print(f"{name}, you have a normal weight.")
        return 0
    else:
        print(f"{name}, you are overweight.")
        return 1

# --- Main Program ---
name = input("Enter your name: ")
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

calculate_bmi(name, height, weight)