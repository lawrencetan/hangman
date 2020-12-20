import random

with open('sowpods.txt', 'r') as f:
  lines = f.readlines()

#print(lines)


words = [ line.strip('\n') for line in lines]

word_to_guess = list(random.choice(words).upper())
#word_to_guess = list('evaporate'.upper())
orig_word_to_guess = set(word_to_guess)
user_guesses = list("_" * len(word_to_guess))
#print("Word to Guess:  ", word_to_guess)
print("Welcome to Hangman!")
print("_ " * len(word_to_guess))
first_guess = []

chance = 6
guess = input("Enter your guess letter: ")
while chance > 1:
    #print("guess: ",guess)
    #print('first guess: ',first_guess)
    if guess.upper() in first_guess:
        print("You already guessed: \"{}\", try another one.".format(guess.upper()))
        guess = ''
    elif guess.upper() in word_to_guess:
        #print("guess is correct")
        index = word_to_guess.index(guess.upper()) #show position of correct guess
        user_guesses[index] = guess.upper() #Place the correct letter from "_" to the correct letter e.g. 
        word_to_guess[index] = "_"
    else:
        print(''.join(user_guesses))
        #print('after join user_guesses')
       # print('guess', guess)
        #print('first_guess', first_guess)
        if guess != '':
            
            first_guess.append(guess.upper())
            #print('before incorrect word_to_guess:', word_to_guess)
            if guess.upper() not in orig_word_to_guess: #if guess is wrong
                #first_guess.append(guess.upper())
                chance -= 1
                print("guess incorrect. {} chance(s) left".format(chance))
            else: #if guess is correct
                print("Nice guess!!")
        guess = input("Enter your guess letter: ")
        #

    if '_' not in user_guesses:
        print('Congrats! YOU WIN!!!')
        print('The word is: {}'.format(''.join(user_guesses)))
        break
if chance == 0:
    print('No chances left. Try again')
		

"""
1. keep track of the letters the player guessed and display a different message if the player tries to guess that letter again.
2. stop the game when all the letters have been guessed correctly


"""