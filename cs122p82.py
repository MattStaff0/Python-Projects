'''
CS 122 Fall 2022 Project 8-2
Author: Matthew Stafford, Lawrence Hall
Credit: none
Description: Password Checker 
'''

import doctest
    

def no_e(password):
    '''
    (password: str) -> bool

    will return True if there is no E or e in password will return false if there is

    >>> no_e('hello')
    False
    >>> no_e('')
    True
    >>> no_e('World22')
    True
    
    '''
    string = password #make string a new variable 
    if 'e' in string:    #seeing if e is in the string 
        return False     # returning false if it has 'e' in it 
    else:
         return True 



def is_upper(password):
    '''
    (password: str) -> bool

    return True if any character in passowrd is an uppercase letter, otherwise
    return False

    >>> is_upper('hEllo')
    True
    >>> is_upper('hello')
    False
    '''
    
    for char in password:   # goes through all characters in password
        if char.isupper():
            return True     # returns True if any characters in password are uppercase

    return False

def two_digits(password):
    '''
    (password: str) -> bool

    return True if the password has 2 digits and return False if it does not

    >>> two_digits('HI2n9p')
    True
    >>> two_digits('Worldsin')
    False
    >>> two_digits('HI2npw')
    False
    '''
    counter = 0   # initialze a counter variable 
    for char in password:  
        if char.isdigit():
            counter += 1     # any time there is a number in a string the counter will rise by 1
    if counter >= 2:      # if counter is greater than or equal to 2 then it returns True if not then False
        return True
    else:
        return False

def special_symbol(password):
    '''
    (password: s) -> bool

    return True if any character in password has one of those characters, if not then return
    False

    >>> special_symbol('mmmmmm@')
    True
    >>> special_symbol('OK99!!')
    True
    >>> special_symbol('%hiiiiiii')
    False
    '''
    if '$' in password:  # uses in to see if there is a special character in password will return True if there is and will return false if there is not
        return True
    elif '!' in password:
        return True
    elif '@' in password:
        return True
    elif '#' in password:
        return True
    else:
        return False
        
        
                
        
        
def five_char(password):
    '''
    (s: str) -> Bool

    Checks if the length of x is more or less than 5, returning true if
    password >= 5

    >>> five_char('hi')
    False
    >>> five_char('world4')
    True
    '''
    counter = 0
    for char in password:
        counter += 1
        
    if counter >= 5: #checks to see if x has more or less than 5 characters 
        return True
    else:
        return False # returns false if the len is not greater than or equal to 5
    
           

def password_check(password):
    '''
    >>> password_check('A99#')
    False
    >>> password_check('')
    False
    >>> password_check('#Qwerty')
    False
    >>> password_check('#qwrty')
    False
    >>> password_check('Qwrty99')
    False
    >>> password_check('%Qwzrty')
    False
    >>> password_check('#Qw9rty')
    False
    >>> password_check('#Qw12rty')
    True
    >>> password_check('OK99!!')
    True
    '''
    fivechar = five_char(password) # turn all functions into variables to set them equal to True 
    noE = no_e(password)
    isUpper = is_upper(password)
    twoDigits = two_digits(password)
    specialSymbol = special_symbol(password)
    if fivechar and noE and isUpper and twoDigits and specialSymbol == True:  # checks to see if all functions are True 
        return True 
    else:
        return False 

def main():
    password = input('Enter password:') # input for password
    password_true = password_check(password) # set equal to vairable to see if it is True or False
    while True:  # loop that will always run if password_true is False and will break if it is True 
        if password_true == True:
            break
        else:
            password = input('Enter a new password:')
    print('Your password is secure.') 
            
        
print(doctest.testmod())
main()

