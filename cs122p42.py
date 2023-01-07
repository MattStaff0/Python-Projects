'''FizzBuzz
Author:Matthew Stafford, C. Science
Credit: CS122 resources only
Description: FizzBuzz game
'''

def fizzbuzz(n):
    '''
    fuction that defines fizzbuzz, uses a for loop to count to parameter n
    then checks i to see if it is divisble by 3 or 5 and prints fizz, buzz,
    fizzbuzz, or i.
    >>>fizzbuzz(3)
    1
    2
    fizz
    '''
    for i in range(1, 1+n):
        if i % 3 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
    return

        
    
        
        
        
    


def main():
    '''main function that calls fizzbuzz'''
    pos_integer = input("Enter a positive integer: ")
    pos_integer = int(pos_integer)
    fizzbuzz(pos_integer)

main()




    

