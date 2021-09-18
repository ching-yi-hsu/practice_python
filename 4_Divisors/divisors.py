num_divides = []
num = int(input("enter a number to find out all the divides : "))

for i in range(1,num):
    if num % i == 0 :
        num_divides.append(i)

print("the list of " ,num , " is " , num_divides)