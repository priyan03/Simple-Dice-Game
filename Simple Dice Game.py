import random 

position_player1 = 0
position_player2 = 0
winning_position = 27
winner = " "
while True:
    input("enter to start.......")
    roll_player1 = random.randint(1,6)
    if position_player1 + roll_player1 <= winning_position:
        position_player1 += roll_player1
        print(f"player 1 rolled{roll_player1},now at the position of {position_player1}")

        if position_player1 == winning_position:
            winner = "player 1"
            break
    roll_player2 = random.randint(1,6)
    if position_player2 + roll_player2 <= winning_position:
        position_player2 += roll_player2
        print(f"Player 2 rolled{roll_player2}, now at the position of {position_player2} ")

        if position_player2 == winning_position:
            winner = "player 2"
            break
 
print(f"******************** THE END ********* {winner} won the game *********************")

