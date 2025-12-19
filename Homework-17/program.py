age = int(input("Enter your age: "))
    
if age < 13:
        print ("Child")
elif age >= 13 and age < 18:
        print ("Teenager")
elif age > 18 and age < 65:
        print ("Adult")
else:
        print ("Elder")


years = int(input("Input number of years: "))

def years_to_days(y):
    return y * 365

def years_to_weeks(y):
    return y * 52

def years_to_months(y):
    return y * 12

def years_to_hours(y):
    return y * 365 * 24

print("Days:", years_to_days(years))
print("Weeks:", years_to_weeks(years))
print("Months:", years_to_months(years))
print("Hous:", years_to_hours(years))


def add (a, b):
    return a + b
def subtract (a, b):
    return a - b
def multiply (a, b):
    return a * b
def divide (a, b):
    return a / b



num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
operator = input("Choose operation (+, -, *, /): ")

if operator == "+":
    result = add(num1, num2)
elif operator == "-":
    result = subtract(num1, num2)
elif operator == "*":
    result = multiply(num1, num2)
elif operator == "/":
    result = divide(num1, num2)
else:
    result = "Invalid operator"
print("Result:", result)
    