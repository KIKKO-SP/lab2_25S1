def calculate_bmi(name, height, weight):
    bmi = weight / (height ** 2)
    rounded_bmi = round(bmi, 2)
    print(f"{name}, your BMI is: {rounded_bmi}")

    if bmi < 18.5:
        print(f"{name}, you are underweight.")
    elif bmi < 25:
        print(f"{name}, you have a normal weight.")
    else:
        print(f"{name}, you are overweight.")

# --- Main Program ---
name = input("Enter your name: ")
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

calculate_bmi(name, height, weight)