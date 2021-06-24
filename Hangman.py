word_list = ["aardvark", "baboon", "camel"]

lives = 6
#Randomly select the word the user will guess from the given word_list
import random
random_word = random.choice(word_list)

#Testing code
print(random_word)

#the random word has to be a list with blanks '_' to represent each letter in the word.
word = []
for letter in random_word:
    word += '_'
print(word)

# Ask the user to guess a letter in the word.(make it lowercase)
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    word_length = len(random_word)  #This is an integer type

    for position in range(word_length):
        letter = random_word[position]
        if guess == letter:
            word[position] = letter

    print(word)

    if '_' not in word:
        end_of_game = True
        print('You win ')

    if guess not in random_word:
        print(f"You guessed the letter {guess}, that's not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('You lose')

#next we will need to ask the user to guess the input until all the blanks are filled correctly
# we will wrap that in a while loop.
# the while loop should only stop running when there are no more blanks in the code.








