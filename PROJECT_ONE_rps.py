#Josh Kallagunta
import random

while True:

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
                print('Invalid Choice')

#Tried to create a way out of the while True loop, but needs a bit more work 
           # end_game = 'y'
           # end_game = input('Do you want to end the game? Type y for yes. ')

          #  if end_game == 'y':
               # print('Thanks for playing!')
              #  break













