import random

random_list_1 = [] 
random_list_2 = [] 
common_list  = []
a1 = random.randint(1,20)
a2 = random.randint(1,20)

random_list_1 = [random.randint(1,50) for i in range(1,a1)]
random_list_2 = [random.randint(1,50) for i in range(1,a2)]
common_list = [n1 for n1 in random_list_1 if n1 in random_list_2]
print("List_1 = " ,sorted(random_list_1) ,"\nList_2 = ", sorted(random_list_2), "\n common list = ", sorted(common_list))
