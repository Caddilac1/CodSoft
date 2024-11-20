import random

game_option = ("rock" , "paper" , "scissors")


win_total = 0
tie_total = 0
lose_total = 0
player_decision = True

while player_decision:

    player_choice = None

    computer_choice = random.choice(game_option)

    while player_choice not in game_option:
        player_choice = input("Enter your choice (rock , paper , scissors): ")


    print(f"You picked: {player_choice}")
    print(f"Computer picked: {computer_choice}")

    if player_choice == computer_choice:
        tie_total += 1
        print("It's a tie!")

    elif player_choice == "paper" and computer_choice == "rock":
        win_total += 1
        print("You win!")    

    elif player_choice == "scissors" and computer_choice == "paper":
        win_total += 1
        print("You win!")

    elif player_choice == "rock" and computer_choice =="scissors":
        win_total += 1
        print("You win. You're a champion!")

    else:
        lose_total += 1
        print("You lose.  Better luck next time!")

    print(f"Scoreboard: Wins: {win_total}, Ties: {tie_total}, Losses: {lose_total}")
    

    play_again = input("Want to play again? (y/n)").lower()

    if not play_again == 'y':
        player_decision = False

print("Thank you for playing") 
print(f"Total win(s): {win_total}")
print(f"Total tie(s): {tie_total}")
print(f"Total losses: {lose_total}") 
