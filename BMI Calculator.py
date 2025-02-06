def get_valid_input(prompt, data_type, min_val, max_val):
    while True:
        try:
            value = data_type(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"Input must be between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("=== BMI Calculator ===")
    weight = get_valid_input("Enter weight (kg): ", float, 1, 300)
    height = get_valid_input("Enter height (m): ", float, 0.5, 2.5)

    bmi = round(weight / (height ** 2), 2)
    category = classify_bmi(bmi)

    print(f"Your BMI is {bmi} ({category}).")


if __name__ == "__main__":
    main()