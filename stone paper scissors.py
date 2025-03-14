import random
choices = ['rock', 'paper', 'scissors']

def check_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()

        if user_choice not in choices:
            print("Invalid choice. Please choose again.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        result = check_winner(user_choice, computer_choice)
        print(result)        
        
        again = input("Do you want to play again? (yes/no): ").lower()
        if again != 'yes':
            break
        
if __name__ == "__main__": 
    play()
