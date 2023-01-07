'''Form and Function, Part 2 (Minimum Payment)
Author:Matthew Stafford, C. Science
Credit: None
Description: Python functions, minimum payment fuction'''
import math

def payment(balance):
    '''finding the minimum payment of a balance using min/max
       where minimum pay is equal to $10 or 2.1% of the balance'''
    minimum_payment = 10
    percent_of_balance = math.ceil(balance * .021)
    if_bal_under_ten = min(minimum_payment, balance)
    final_payment = max(if_bal_under_ten, percent_of_balance)
    print('Minimum payment for balance $', balance, 'is $', final_payment,'.')
    return


