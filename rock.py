import random

score_player1 = 0 
score_player2 = 0
while True: 
    player1 = input("wanna play ? Rock/Paper/Scissor: ")
    print(player1)
    player2 = random.choice(["rock","paper","scissor"])
    print(player2)
    
    if player1 == player2:
        
        print ("Try Again")
        print (f'Score : {score_player1}-{score_player2}')
        
    elif player1 == "rock" and player2 == "paper":
        print("player 2 as paper wins")
        score_player2 += 1
        print (f'Score : {score_player1}-{score_player2}')

    elif player1 == "rock" and player2 == "scissor":
        print("player 1 as rock wins")
        score_player1 += 1
        print (f'Score : {score_player1}-{score_player2}')
    
    elif player1 == "paper"  and player2 == "scissor":
        print("player 2 as scissor wins")
        score_player2 += 1
        print (f'Score : {score_player1}-{score_player2}')

    elif player1 == "paper"  and player2 == "rock":
        print("player 1 as paper wins")
        score_player1 += 1
        print (f'Score : {score_player1}-{score_player2}')
   
    elif player1 == "scissor"  and player2 == "rock":
        print("player 2 as rock wins")
        score_player2 += 1
        print (f'Score : {score_player1}-{score_player2}')
    elif player1 == "scissor"  and player2 == "paper":
        print("player 1 as scissor wins")
        score_player1 += 1
        print (f'Score : {score_player1}-{score_player2}')
    else:
        print("rock/paper/scissor only")
        break
    