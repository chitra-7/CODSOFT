import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def decide_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "win"
    else:
        return "lose"

def show_result(user, computer, result):
    print("\n--- RESULT ---")
    print(f"You chose: {user}")
    print(f"Computer chose: {computer}")
    if result == "win":
        print("🎉 You win!")
    elif result == "lose":
        print("😢 You lose.")
    else:
        print("🤝 It's a tie!")

# Main Game
user_score = 0
computer_score = 0

print("=== ROCK, PAPER, SCISSORS GAME ===")

while True:
    print("\nChoose one: rock, paper, scissors")
    user_choice = input("Your choice: ").lower()

    if user_choice not in ["rock", "paper", "scissors"]:
        print("❌ Invalid choice! Please choose again.")
        continue

    comp_choice = get_computer_choice()
    result = decide_winner(user_choice, comp_choice)

    if result == "win":
        user_score += 1
    elif result == "lose":
        computer_score += 1

    show_result(user_choice, comp_choice, result)

    print(f"\nScoreboard: You - {user_score} | Computer - {computer_score}")

    play_again = input("\nPlay another round? (yes/no): ").lower()
    if play_again != "yes":
        print("\nThanks for playing! Final Score:")
        print(f"You: {user_score} | Computer: {computer_score}")
        break
