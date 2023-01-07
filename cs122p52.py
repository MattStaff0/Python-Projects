'''Einstein's Math Trick
Author:Matthew Stafford, C. Science
Credit: CS122 resources only
Description: Writing a program that entails Einstein's math trick
'''

def check_positive_int(n):
    ''' checks if an interger n is postive and then returns true if it is
    >>>check_positive_int(10)
    returns True
    '''
    if n >= 0:
        return True
    else:
        return False

def check_3_digits(n):
    ''' checks if an interger n has 3 digits and then returns true if it does
    >>>check_3_digits(100)
    returns True
    '''
    if n > 99 and n < 1000:
        return True
    else:
        return False

    
def check_end_digits(n):
    ''' checks if the integer n's frist and last digit are different and then returns true if they are
    >>>check_end_digits(102)
    returns True
    '''
    last_digit = (n % 10)
    first_digit = (n // 100)
    if last_digit == first_digit:
        return False
    else:
        return True

def check_number(n):
    '''function that returns true if all three auxiliry functions are true'''
    if check_positive_int(n) == True and check_3_digits(n) == True and check_end_digits(n) == True:
        return True
    else:
        return False


def reverse(n): 
    '''
    reverses the order of the integer n and returns that value
    >>>reverse(345)
    543
    '''
    number = 0
    for i in range(3):
        number2 = n % 10
        number = (number * 10) + number2
        n //= 10
    return number

def einstein(n):
    '''
    function that does the einstein math trick
    >>>einstein(768)
    1089
    '''
    num = max(reverse(n), n) - min(reverse(n), n)
    final_num = num + reverse(num)
    return final_num

def main():
    '''driver for einstein program'''
    magic_number = 1089
    n = input('Enter a 3-digit positive number (different 1st and last digits): ')
    n = int(n)
    
    valid_number = check_number(n)
    if not valid_number: print('Invalid number')
    else:
        print(einstein(n))
    
    return

main()

    
