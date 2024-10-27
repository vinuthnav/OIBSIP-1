def cal_bmi(weight, height):
    bmi = weight /( (height /100)*2)
    return bmi

def bmi_cat(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("Welcome to the BMI Calculator!!!")
    try:
        w = float(input("Enter your weight in kilograms: "))
        h = float(input("Enter your height in centimeters: "))
        bmi = cal_bmi(w, h)
        cat = bmi_cat(bmi)
        print(f"Your BMI is: {bmi:.2f}")
        print(f"You are classified as: {cat}")
    except ValueError:
        print("Please enter valid numeric values for weight and height.")

if __name__ == "__main__":
    main()
