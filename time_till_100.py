'''Create a program that asks the user to enter their name and their age.
 Print out a message addressed to them that tells them the year that they will turn 100 years old.'''
import datetime

name = input("Hello, please input your name: " )
print("hello", name, "!")

age = input("please input your age to find out what year you will turn the big 100: " )

now = datetime.datetime.now()
years_till_100 = 100 - int(age)
year_of_100 = now.year + years_till_100
print("You will turn 100 in year:", year_of_100)
