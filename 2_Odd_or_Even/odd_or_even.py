num = int(input("enter a lucky number : "))
check = int(input("enter a number to divide by : "))

if num % 4 == 0 :
    print(num, " is a multiple of 4")
elif num % 2 == 0 :
    print(num, " is even number")
else:
    print(num, " is odd number")

if num % check == 0 :
    print(num, " divides evenly by ", check)
else :
    print(num, "does not divide evenly by ", check)