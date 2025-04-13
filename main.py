#stuff needed to make the game work
import random
import hangman_words
import hangman_art

lives = 6

print(hangman_art.logo)
#Grabs a random word from the huge list of wwords
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)
#makes placeholders according to the lenght of the word
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)
#stores the guessed letters 
game_over = False
correct_letters = []
guessed_letters = []

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()
    #Guess a letter and refreshed the display
    display = ""
    #If they already guessed the letter they are told so
    if guess in guessed_letters:
        print("You've already guessed this letter, try another.")
    else:
        guessed_letters.append(guess)
    # if they guessed a correct letter it gets added 
    # and appended to the lists under game_over
    # Guess letters replaces the _ and if the letter
    #is not guessed it just shows _
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)
    #if the guessed letter is not in the word 
    #They lose one life and the art gets updated
    # 0 lives is game over 
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True

            print(f"***********************YOU LOSE**********************"
                  f"\nThe word was {chosen_word}")
    #if all _ is filled they win since all the 
    #letters have been guessed. 
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(hangman_art.stages[lives])
