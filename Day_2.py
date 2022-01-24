***************************************************************************************"""
Exercise 1 - Data Types
Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
***************************************************************************************"""
two_digit_number = input("Type a two digit number: ")
two_letter_str = str(two_digit_number);
a = int(two_letter_str[0])
b = int(two_letter_str[1])
sum = a+b
print(sum)



***************************************************************************************"""
Exercise 2 - BMI Calculator
Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and 
a short person both weigh the same amount, the short person is usually more overweight.
The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
***************************************************************************************"""
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
h = float(height) * float(height)
w = int(weight)

bmi = w/h 

print(int(bmi))



***************************************************************************************"""
Exercise 3 - Life in Weeks
Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
It will take your current age as the input and output a message with our time left in this format:
You have x days, y weeks, and z months left.
Where x, y and z are replaced with the actual calculated numbers.
***************************************************************************************"""
age = input("What is your current age?")
age_left = 90 - int(age);
day = str(age_left * 365)
week = str(age_left * 52)
month = str(age_left * 12)
print("you have " + str(age_left) + " left. \n")
print("You have " + day + " days, " + week + " weeks, and " + month + " months left.")


***************************************************************************************"""
Final Project - Tip Calculator
How it works
If the bill was $150.00, split between 5 people, with 12% tip. 
Each person should pay (150.00 / 5) * 1.12 = 33.6
Format the result to 2 decimal places = 33.60
Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
Write your code below this line 👇
***************************************************************************************"""
print("Welcome to the Tip Calculator")
total_bill = float(input("What was your total bill? $"))
Percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_person = int(input("How many people to split the bill? "))
tip = round(float((total_bill/num_person) * (Percentage_tip / 100)), 2)
print(f"Each person should pay {tip} ")
