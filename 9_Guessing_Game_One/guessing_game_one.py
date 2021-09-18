import random

def guess_game() :
    rnum = random.randint(1,100)
    high_num = 100
    low_num = 1
    c_num = 0
    gnum = input("enter a number between 1 to 100 to guessing the right one or type exit to end game.  ")

    while gnum != "exit" :
        gnum = int(gnum)
        c_num = c_num + 1
        if rnum == gnum :
            print("you are guess right number!, after " ,c_num," times")
            gnum = "exit"
        elif gnum > rnum :
            high_num = gnum           
            print("Wrong number ! Between " , low_num, " ~ " , high_num , "you have been guess " , c_num, " times")
            gnum = input("enter a number  or type exit to end game ")
        elif gnum < rnum :
            low_num = gnum
            print("Wrong number ! Between " , low_num, " ~ " , high_num , "you have been guess " , c_num, " times")
            gnum = input("enter a number  or type exit to end game ")

start_game = input("would you like to play a guessing number game ? N/Y ?   ")
while start_game == "Y" or start_game == "y":
    guess_game()
    start_game = input("would you like to play a guessing number game ? N/Y ?   ")