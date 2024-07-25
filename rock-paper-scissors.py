import random

def get_computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
        return "You win!"
    else:
        return "You lose!"

def main():
    user_score = 0
    computer_score = 0
    
    print("Welcome to Rock, Paper, Scissors!")

    while True:
        user_choice = input("Choose Rock, Paper, or Scissors (or 'quit' to stop): ").capitalize()

        if user_choice == 'Quit':
            break
        elif user_choice not in ['Rock', 'Paper', 'Scissors']:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1

        print(f"Score - You: {user_score}, Computer: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print(f"Final Score - You: {user_score}, Computer: {computer_score}")
    print("Thank you for playing!")

if __name__ == "__main__":
    main()


