"""

INSTITUTION: UDEMY.COM

COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021

INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 3
EXERCISE: 3-3 Leap Year
LEVEL: Beginner

INSTRUCTIONS:

    Write a program that works out whether if a given year is a leap year. 
    A normal year has 365 days, leap years have 366, with an extra day in February.

    This is how you work out whether if a particular year is a leap year:

        on every year that is evenly divisible by 4
            **except** every year that is evenly divisible by 100
            **unless** the year is also evenly divisible by 400`

    Use the code provided -- do not change the existing code!

    CODE:

        year = int(input("Which year do you want to check? "))

        # WRITE YOUR CODE HERE

"""

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
        print("Leap year.")