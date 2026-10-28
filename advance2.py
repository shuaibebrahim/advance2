# -------------------------------------------
# Advanced Python Challenge: Exercise 02 Operators and Conditionals
# -------------------------------------------

# Overview:
# This exercise challenges your understanding of Python operators, conditionals, and input handling.
# Complete each section with the required logic, using good variable names and adding comments where necessary.

# -------------------------------------------
# Question 1: Multi-Step Arithmetic Operations
# -------------------------------------------

# Task:
# Use compound arithmetic operators to modify values of a, b, and c.
# Then calculate the square root of the sum of their squares.
# Tip: Use the math module.

import math

# Start with some base values
a = 5
b = 10
c = 7

# TODO: Add 3 to a using +=
# TODO: Multiply b by 2 using *=
# TODO: Modulo c by 4 using %=
a += 3
print("Add 3 to a: 5 + 3 =", a)
b *= 2
print("Multiply b by 2: 10 * 2 = 20")
c %= 4
print("Modulo c by 4: 7 % 4 =", c)
# TODO: Calculate the square root of (a^2 + b^2 + c^2)
result = math.sqrt(a**2 + b**2 + c**2)
# TODO: Print the final result rounded to 2 decimal places
print("Square root of (a^2 + b^2 + c^2):", round(result, 2))


# -------------------------------------------
# Question 2: Complex Conditional Evaluation
# -------------------------------------------

# Task:
# Ask the user to input three integers (x, y, z).
# Then evaluate and print whether:
# - x is even
# - y is positive
# - z is between 10 and 50
# Use logical operators to combine the conditions.

# Tip: Use and/or to join conditions.

# TODO: Input x, y, z
# TODO: Create conditions:
#   is_even = True if x is even
#   is_positive = True if y > 0
#   is_in_range = True if z between 10 and 50
# TODO: Create final_condition = is_even and is_positive and is_in_range
# TODO: Print final_condition
x = int(input("Enter an integer for x: "))  
y = int(input("Enter an integer for y: "))  
z = int(input("Enter an integer for z: "))  

is_even = x % 2 == 0
is_positive = y > 0
is_in_range = 10 <= z <= 50
final_condition = is_even and is_positive and is_in_range

print("Is x even?", is_even)
print("Is y positive?", is_positive)
print("Is z between 10 and 50?", is_in_range)
print("Final condition (x is even AND y is positive AND z is in range):", final_condition)
# -------------------------------------------
# Question 3: Grading with Adjustments
# -------------------------------------------

# Task:
# Ask the user for their base score, then apply:
# - bonus points (+5)
# - late penalty (-10)
# Final score must not exceed 100 or drop below 0.
# Then assign a grade.

# Tip: Use min() and max() to constrain the score.

# TODO: Input score from user
# TODO: Apply adjustments
# TODO: Clamp score between 0 and 100
# TODO: Use if-elif-else to determine grade and print it
# Ask the user to enter their base score
base_score = float(input("Enter your base score: "))

# Apply bonus points and late penalty
score = base_score + 5 - 10

# Keep the final score between 0 and 100
score = max(0, min(100, score))

# Display the final score
print("Final score:", score)

# Assign a grade
if score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    grade = "C"
elif score >= 50:
    grade = "D"
else:
    grade = "F"

print("Your grade is:", grade)



# -------------------------------------------
# Question 4: Advanced Calculator
# -------------------------------------------

# Task:
# Ask the user to input two numbers and an operation (+, -, *, /, %, **).
# Handle division/modulus by zero with error checking.
# Perform the operation and print the result.

# Tip: Use try-except and elif branches for each operation.

# TODO: Input num1, num2
# TODO: Input operation
# TODO: Match operation using if-elif
# TODO: Handle division/modulus by zero with try-except
# TODO: Print result
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter an operation (+, -, *, /, %, **): ")

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = num1 / num2
    elif operation == '%':
        if num2 == 0:
            print("Error: Cannot perform modulus by zero.")
        else:
            result = num1 % num2
    elif operation == '**':
        result = num1 ** num2
    else:
        print("Error: Invalid operation.")

    print("Result:", result)
except ValueError as e:
    print("Error:", e)