#Josh Kallagunta
import random

#User input that makes the game True, so that it will keep playing
#Chosing 'n' will end the game
keep_going = 'y'
end_game = 'n'

while keep_going == 'y':

    #Setting up the game, getting user input, making it lowercase to make it work with the list 
	user_input = str(input('\nChose rock, paper, or sissors! '))
	user_input = user_input.lower()

    #Printing the user choice of the game 
	print('You chose: ', user_input)

    #List of the valid options that can be made 
	valid_moves = ['rock', 'paper', 'scissors']

    #Varible that randomly chooses a move fron the valid_moves list 
    #Will be used to see if the computer or player wins 
	computer_choice = random.choice(valid_moves)

    #Printing the computer choice 
	print("The game chose: ", computer_choice)

    #If statement checks if the user input is in the list "valid_moves"
    #if it is, it will continue on and play the game
    #using if and elif statements to check if certain conditions are met, 
    #depending on the user input and computer, it will print out a result 
	if user_input in valid_moves:
            if user_input == computer_choice:
                print('Game Tied!')
            elif user_input == 'rock' and computer_choice == 'sissors':
                print('Congrats, You win!')
            elif user_input == 'rock' and computer_choice == 'paper':
                print('Sorry, You lose.')
            elif user_input == 'paper' and computer_choice == 'rock':
                print('Congrats, You win!')
            elif user_input == 'paper' and computer_choice == 'scissors':
                print('Sorry, You lose.')
            elif user_input == 'scissors' and computer_choice == 'paper':
                print('Congrats, You win!')
            elif user_input == 'scissors' and computer_choice == 'rock':
                print('Sorry, You lose.')
            else:
                pass
            

            #This lets the user either keep playing or stop playing the game
            #'y' will keep it going, 'n' will stop the game 
            keep_going = input('Do you want to play again? Type "y" for yes. Type "n" for no. ')

            if keep_going == 'y':
               print('Continue Playing! ')
            elif end_game == 'n':
                print('Thanks for playing! ')
                break


#fixed issues with the program











