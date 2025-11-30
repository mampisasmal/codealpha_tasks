import random
words = ["python", "hangman", "computer", "programming", "algorithm","function","software","variable","condition"]
word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6
display = ["_"] * len(word)

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses allowed.")
print("Word:", " ".join(display))

while incorrect_guesses < max_incorrect and "_" in display:
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
        print("Correct!")
    else:
        incorrect_guesses += 1
        print("Incorrect!")

    print("Word:", " ".join(display))
    print("Incorrect guesses:", incorrect_guesses)
    print("Guessed letters:", ", ".join(guessed_letters))

if "_" not in display:
    print("Congratulations! You guessed the word:", word)
else:
    print("Game over! The word was:", word)
