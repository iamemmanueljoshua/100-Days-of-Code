********************************************************************************************************"""
BMI Calculator
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
It should tell them the interpretation of their BMI based on the BMI value.
Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.
***********************************************************************************************************"""

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / (height ** 2))

if bmi < 18.5: 
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi > 18.5 and bmi < 25:
     print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi > 25 and bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi > 30 and bmi <= 35:
    print(f"Your BMI is {bmi}, you are obese.")
elif bmi > 35:
    print(f"Your BMI is {bmi}, you are clinically obese.")
    
***********************************************************************************************************"""
Odd or Even 
Write a program that works out whether if a given number is an odd or even number.
Even numbers can be divided by 2 with no remainder.
e.g. 86 is even because 86 ÷ 2 = 43
43 does not have any decimal places. Therefore the division is clean.
e.g. 59 is odd because 59 ÷ 2 = 29.5
29.5 is not a whole number, it has decimal places. Therefore there is a remainder of 0.5, so the division is not clean.
The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division.
***********************************************************************************************************"""

number = int(input("Which number do you want to check? "))
if number % 2 != 0:
    print("This is an odd number.")
else:
    print("This is an even number.")

    
***********************************************************************************************************"""
Exercise 3 - Leap Year
Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, 
with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice:
https://www.youtube.com/watch?v=xX96xng7sAE
This is how you work out whether if a particular year is a leap year.
on every year that is evenly divisible by 4 
**except** every year that is evenly divisible by 100 
**unless** the year is also evenly divisible by 400
***********************************************************************************************************"""

year = int(input("Which year do you want to check? "))
if year % 4 == 0 or year % 400 == 0 and year % 100 != 0 :
    print("Leap year.")
else:
    print("Not leap year.")  

    
***********************************************************************************************************"""
Exercise 4 - Pizza Order Practice
Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
Based on a user's order, work out their final bill.
Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25
Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: + $1

***********************************************************************************************************"""

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
    bill = 15
elif size == "M":
    bill  = 20
elif size == "L":
    bill = 25

if add_pepperoni == "Y": 
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")

***********************************************************************************************************"""
Exercise 5 - Love Calculator
You are going to write a program that tests the compatibility between two people.
To work out the love score between two people:
Take both people's names and check for the number of times the letters in the word TRUE occurs. 
Then check for the number of times the letters in the word LOVE occurs. 
Then combine these numbers to make a 2 digit number.
For Love Scores less than 10 or greater than 90, the message should be:
"Your score is **x**, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:
"Your score is **y**, you are alright together."
Otherwise, the message will just be their score. e.g.:
"Your score is **z**."

***********************************************************************************************************"""

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

added_names = name1.lower() + "" + name2 .lower()
added_names

score_1 = 0

score_1 += added_names.count("t")
score_1 += added_names.count("r")
score_1 += added_names.count("u")
score_1 += added_names.count("e")

score_2 = 0
score_2 += added_names.count("l")
score_2 += added_names.count("o")
score_2 += added_names.count("v")
score_2 += added_names.count("e")

score = int(str(score_1) + str(score_2))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
