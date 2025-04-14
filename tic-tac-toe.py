import random

def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    while True:
        user_input = input("Enter your choice (rock/paper/scissors): ").lower()
        if user_input in choices:
            return user_input
        else:
            print("❌ Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    print(f"\n🧍 You chose: {user}")
    print(f"🤖 Computer chose: {computer}")

    if user == computer:
        return "🤝 It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "🎉 You win!"
    else:
        return "💻 Computer wins!"

def play_game():
    print("=== Rock, Paper, Scissors ===")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("\n🔁 Play again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            print("👋 Thanks for playing!")
            break
        print("\n--------------------------")

if _name_ == "_main_":
    play_game()