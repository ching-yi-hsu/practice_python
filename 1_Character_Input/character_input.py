import datetime

name = input("enter your name : ")
age = input("enter your age : ")

year_now = int(datetime.datetime.now().year)
years_of_turn_100 = 100 - int(age)
year_of_100 = year_now + years_of_turn_100

print(name + " you will turn to 100 years old at " + str(year_of_100))
