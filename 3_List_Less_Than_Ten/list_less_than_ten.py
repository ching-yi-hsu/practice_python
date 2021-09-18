import random

random_num_arr = []
list_num = random.randint(1,20)
num_less_than_5 = []

for i in range(list_num):
    num = random.randint(1,20)
    random_num_arr.append(num)

for num in random_num_arr :
    if num < 5 :
        num_less_than_5.append(num)
    

print("random number list : " ,random_num_arr)
print("numbers less than 5 list of ", sorted(num_less_than_5))
