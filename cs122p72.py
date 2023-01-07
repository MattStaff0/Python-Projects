'''
CS 122 Fall 2022 Project 7-2
Author: Matthew Stafford, Lawrence Hall
Credit: none
Description: Bugs, Bugs, Bugs
'''
import doctest
####
#(1) RAT WEIGHT
####
def rats(weight, p):
    '''(weight: float, p: float) -> None
    Print number of weeks it will
    take for a rat to weigh 2 times
    as much as its original weight
    (weight) if it gains weight at
    rate p percent per week.
    >>> rats(10, 10)
    The rat weighs 21.4 after 8 weeks.
    '''
    weeks = 0
    rate = p * .01
    og_weight = weight # make a new variable to mkae an orignal and a new weight 
    while weight < (2 * og_weight): # add a colon and swap weight variable for the of_weight variable
        weight += weight * rate
        weeks = weeks + 1 # weeks = weeks plus 1, to use the same variable 
    weight = round(weight, 1)
    print(f'The rat weighs {weight} after {weeks} weeks.')
    return
####
#(2) MINUTES TO YEARS
####
def minutesToHours(minutes):
    '''(minutes: number) -> float
    convert input minutes to hours;
    return hours
    >>> minutesToHours(60)
    1.0
    >>> minutesToHours(90)
    1.5
    >>> minutesToHours(0)
    0.0
    '''
    hours = minutes / 60
    hours = round(hours, 2)
    print(hours)
    return

def hoursToDays(hours):
    '''(hours: int) -> float
    convert input hours to days;
    return days
    >>> hoursToDays(24)
    1.0
    >>> hoursToDays(100)
    4.17
    >>> hoursToDays(0)
    0.0
    '''
    days = hours / 24
    days = round(days, 2) # round days variable to 2 decimal points instead of 1
    return days
def daysToYears(days):
    '''(days: int) -> float
    convert input days to yearss;
    return years
    >>> daysToYears(365)
    1.0
    >>> daysToYears(100)
    0.27
    >>> daysToYears(0)
    0.0
    '''
    # remove days = 365 variable as the function has a parameter used for days 
    years = days / 365
    years = round(years, 2)
    return years
def minutesToYears(m):
    '''(m: int) -> float
    input number m minutes is converted to
    equivalent number of years. return years.
    call auxiliary functions to do each step
    >>> minutesToYears(525600)
    1.0
    >>> minutesToYears(5256000)
    10.0
    >>> minutesToYears(394200)
    0.75
    >>> minutesToYears(0)
    0.0
'''
    # give functions variable assignments so that the main function can return values
    y = minutesToHours(m)
    y = hoursToDays(y)
    y = daysToYears(y)
    # round variable 2 decimal places
    y = round(y, 2)

    return y
####
#(3) COUNTING VOWELS
####
def count_vowels(s):
    '''(s: str) -> int
    Return number of vowels in s.
    >>> count_vowels('The quick brown fox')
    5
    >>> count_vowels('University of Oregon')
    8
    >>> count_vowels('Hello World')
    3
    >>> count_vowels('HELLO WORLD')
    3
    >>> count_vowels('Python')
    1
    >>> count_vowels('CCC')
    0
    more examples of use/test cases go here
    '''
    # remove vowels variable
    ctr = 0
    # change ch to letters
    for letters in s:
        # if statements for all possible vowels instead of using the vowels variable 
        if letters == 'a' or letters == 'e' or letters == 'i' or letters == 'o' or letters == 'u' or letters == 'A' or letters == 'E' or letters == 'I' or letters == 'O' or letters == 'U':
            # change variable name to ctr as need to use the same variable name 
            ctr += 1

            
    return ctr


####
#(4) REVERSE? (TEXT CH. 8)
####
def is_reverse(word1, word2):
    '''(word1: str, word2: str) -> bool
    compare two words and return True if
    one is the reverse of the other;
    case matters
    >>> is_reverse('abc', 'cba')
    True
    >>> is_reverse('abc', 'CBA')
    False
    >>> is_reverse('a', 'a')
    True
    >>> is_reverse('abcc', 'abcc')
    False
    >>> is_reverse('yes', 'no')

    False
    >>> is_reverse('abb', 'bbb')
    False
    >>> is_reverse('abc', 'zba')
    False
    '''
    if len(word1) != len(word2):
        return False
        i= 0
        j = len(word2)
    while j > 0:
        # changed j to j - 1 to account for fact that it starts at zero
        if word1[i] != word2[j - 1]:
            return False
        i += 1
        j -= 1
        
    return True

print(doctest.testmod())
