"""
Simple BMI Calculator

"""

print("Welcome to the powerful BMI application. let's start.. ")

while True:
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
    except ValueError:
        print('Invalid input. Please enter numbers.')
        continue
    
    if weight <= 0 or height <= 0:
        print('Invalid input. Numbers must be greater than zero.')
        continue
    
    bmi = round(weight / (height**2), 2)
    print(f'Your bmi is {bmi}')
    
    if bmi < 18.5:
        print('Underweight')
    elif 18.5 <= bmi < 25:
        print('Normal weight')
    elif 25 <= bmi < 30:
        print('Overweight')
    elif bmi >= 30:
        print('Obesity')
        
    again = input('Do you want to calculate again? Press any key for Yes and n for No: ')

    if again.strip().lower() == 'n':
        print('Goodbye.')
        break
