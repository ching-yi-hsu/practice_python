import random

random_list = []
random_num = random.randint(5,15)
random_list = [ random.randint(1,20)  for x in range(1,random_num)   ]

even_list = [x for x in random_list if x % 2 == 0]

print ( "random list : " , sorted(random_list) ,"\neven list : ", sorted(even_list))