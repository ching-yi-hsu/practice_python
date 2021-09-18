
def RPS_game():
    rock = 1
    paper = 2
    scissors = 3

    player_1 = int((input("you are play1 , rock = 1, paper = 2, scissors = 3, please enter a number : ")))
    player_2 = int((input("you are play2 , rock = 1, paper = 2, scissors = 3, please enter a number : ")))

    if player_1 == player_2 :
        print("this game is even")
    elif player_1 <= 2 and player_2 <= 2 :
        if player_1 > player_2 :
            print(" Play1 won !")
        else :
            print("play2 won !")
    elif player_1 == 3 or player_2 == 3 :
        if player_1 == 1 :
            print("Play1 won !")
        elif player_2 == 2 :
            print("play1 Won!")
        else:
            print("Play2 won!")

play_game = str(input("would you like to start the game ? Y/N ? "))
while play_game == "Y" or play_game == "y" :
    RPS_game()
    play_game = input("would you like to start the game again ? Y/N ? ")
