import random

def get_computer_choice():
    """Get a random choice for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])

def get_player_choice():
    """Get the player's choice with validation."""
    while True:
        choice = input("Enter rock, paper, or scissors: ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        print("Invalid choice. Please try again.")

def determine_winner(player, computer):
    """Determine the winner of the round."""
    if player == computer:
        return "tie"
    
    if (player == 'rock' and computer == 'scissors') or \
       (player == 'paper' and computer == 'rock') or \
       (player == 'scissors' and computer == 'paper'):
        return "player"
    
    return "computer"

def play_game():
    """Main game loop."""
    print("Welcome to Rock, Paper, Scissors!")
    score = {'player': 0, 'computer': 0, 'ties': 0}
    
    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        
        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        
        winner = determine_winner(player_choice, computer_choice)
        
        if winner == "tie":
            print("It's a tie!")
            score['ties'] += 1
        elif winner == "player":
            print("You win!")
            score['player'] += 1
        else:
            print("Computer wins!")
            score['computer'] += 1
        
        print(f"\nScore - You: {score['player']}, Computer: {score['computer']}, Ties: {score['ties']}")
        
        play_again = input("\nPlay again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()