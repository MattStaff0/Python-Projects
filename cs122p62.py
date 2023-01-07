'''In the loop, Rock Paper Scissors  
Author:Matthew Stafford, C. Science
Credit: CS122 resources only
Description: Writing a program that plays rock paper scissors
'''

import random
def rps():
    '''
Function that runs a game of rock, paper, scissors
>>>rps()
Side 1 is rock and Side 2 is scissors
The winner is Side 1!
    '''
    #defining rock paper scissor variable as list
    rps = ['rock', 'paper', 'scissors']
    while True:
        #defines each side as a random choice of either rock, paper, or scissors from the rps list
        side1 = random.choice(rps)
        side2 = random.choice(rps)
        
        print('Side 1 is', side1, 'and Side 2 is', side2)
        
        if side1 == side2:
            print('tie, playing again')
        elif side1 == 'rock' and side2 == 'scissors':
            print('The winner is Side 1!')
            break
        elif side1 == 'scissors' and side2 == 'rock':
            print('The winner is Side 2!')
            break
        elif side1 == 'rock' and side2 == 'paper':
            print('The winner is Side 2!')
            break
        elif side1 == 'paper' and side2 == 'rock':
            print('The winner is Side 1!')
            break
        elif side1 == 'paper' and side2 == 'scissors':
            print('The winner is Side 2!')
            break
        elif side1 == 'scissors' and side2 == 'paper':
            print('The winner is Side 1!')
            break
    return

rps()
            
                

