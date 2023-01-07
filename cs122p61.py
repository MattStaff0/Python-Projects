'''Approximate Sqaure Root 
Author:Matthew Stafford, C. Science
Credit: CS122 resources only
Description: Writing a program that approximates the square root of a number
'''
import math

def mysqrt(a):
    '''
function that calculates estimate of square root of parameter a and returns value of x
>>>mysqrt(9):
1
3.0
    '''
    # defining variables
    x = 1
    epsilon = .0001

    # while loop that breaks if equation returns values: x = y or y - x <= epsilon
    while True:
        y = (x + a/x) / 2
        if x == y:
            break
        elif (abs(y - x) <= epsilon):
            break
        # changing value of x equal to y
        x = y

    # return value of x  
    return x
       

def square_root_compare():
    '''
function that prints: value of a from 1-10, the square root of "a" according to mysqrt function,
the square root of "a" using the math square root function and the difference between those two values
    '''
    # for loop utilizing f string to print values in 4 columns and 10 rows
    for i in range(1, 11):
        print(f'{i:0}, {mysqrt(i):20}, {math.sqrt(i):20}, {mysqrt(i) - math.sqrt(i):20}')
    return

# provided code
def main():
 '''driver'''
 # print table header
 print('\nSquare Root Calculator\n')
 print(f'{"a":5}{"mysqrt(a)":25}{"math.sqrt(a)":25}{"diff":25}')
 
 square_root_compare()
 return

# execute main function      
main()




