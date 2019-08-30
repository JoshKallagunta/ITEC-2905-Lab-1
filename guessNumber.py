import random
class Guess:
    def __init__(self, num= (1,20)):
        self.num = num

    def number_guess(self):
        return random.randint(1, self.num)



num = random.randint(1,20)

keep_going='y'

while keep_going =='y':
    user_guess = int(input("Guess a number from 1-20 "))
        
    if num < user_guess:
        print('Guess is to high')
    elif num > user_guess:
        print('Guess is too low ')
    elif num == user_guess:  
        print('Got it! ')
        break 


    keep_going=input('do you want to try again(enter y for yes)')





