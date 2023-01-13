from random import randint
player_wins = 0
computer_wins = 0

def display_header():
    print(f"player Score: {player_wins} Computer Score: {computer_wins}")
    print("...Rock...")
    print("...Paper...")
    print("...Scissors...")

    player = input("player 1, make your move: ").lower()
    rand_num = random.randint(0,2)
    if (rand_num == 0):
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else:
        computer = "scissors"
    print(f"Computer plays {computer}" )

    if player == computer:
        print("It's a tie")
    elif player == "rock":
        if computer == "paper":
           print("Computer wins!")
           computer_wins += 1
    else:
        print("Player wins!")
    elif player == "paper":
        if computer == "rock":
          print("player wins!")
          player_wins += 1
    else:
            print("computer wins!")
    elif (player == "scissors"):
        if (computer == "rock"):
        print("Computer wins!")
         computer_wins += 1
    else:
        print("You wins!")
    else:
    print("please eneter a valid move!  ")

    def start_game(winning_score):
        while player_wins < winning-score and computer < winning_score:
            display_header()

            player = input("(Enter your choice): ").lower()
            if player == "quit" or player == "q":
                break
            computer = pick_computer_move()
            calculate_winner(player,computer)

    def display_winner():
        if player_wins > computer_wins:
            print("CONGRATS, YOU WON"!)
        elif player_wins == computer_wins:
            print("IT'S A TIE")
        else:
            print("OH NO :(THE COMPUTER WON..")

 start_game(3)
 display_winner()
