# PROJECT 02: NUMBER GUESSING GAME & WORD COUNTER
import random
import string
from collections import Counter
# Number guessing game
def guessing_game():
    best_score = 100
    while True:
        secret_number = random.randint(1, 100)
        attempts = 10
        score = 100
        won = False
        print("\nGuess a number between 1 and 100")
        print("You have 10 attempts.")
        while attempts > 0:
            try:
                guess = int(input("Enter your guess: "))
                if guess < 1 or guess > 100:
                    print("Enter a number between 1 and 100.")
                    continue
            except ValueError:
                print("Invalid input! Enter a whole number.")
                continue
            attempts -= 1
            if guess == secret_number:
                print("Congratulations! Correct guess.")
                won = True
                break
            elif guess > secret_number:
                print("Too high!")
            else:
                print("Too low!")
            score = max(0, score - 10)
            print("Attempts remaining:", attempts)
        if not won:
            score = 0
            print("Game over! The number was:", secret_number)
        print("Your score:", score)
        if score > best_score or best_score == 100:
          best_score = score
        print("Best score:", best_score)
        again = input("Play again? (yes/no): ").lower()
        if again != "yes":
            break
# Word counter
def count_words(path):
    try:
        with open(path, encoding="utf-8") as file:
            text = file.read().lower()
    except FileNotFoundError:
        print("File not found:", path)
        return
    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )
    words = text.split()
    counts = Counter(words)
    print("\n===== WORD COUNT RESULTS =====")
    print("Total words:", sum(counts.values()))
    print("Unique words:", len(counts))
    print("\nTop 10 Common Words:")
    print("------------------------")
    for word, number in counts.most_common(10):
        print(f"{word:<15}{number:>5}")
# Main menu
def main():
    while True:
        print("\n===== PROJECT 02 =====")
        print("1. Number Guessing Game")
        print("2. Word Counter")
        print("3. Quit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            guessing_game()
        elif choice == "2":
            path = input("Enter text file name: ").strip()
            count_words(path)
        elif choice == "3":
            print("Thank you! Goodbye.")
            break
        else:
            print("Invalid choice! Select 1, 2 or 3.")
if __name__ == "__main__":
    main()
