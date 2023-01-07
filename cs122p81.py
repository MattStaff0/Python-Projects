'''
CS 122 Fall 2022 Project 8-1
Author: Matthew Stafford, Lawrence Hall
Credit: none
Description: Fun with files 
'''

import doctest

def vowel_ctr(word):
    '''
    (word: str) -> int

    return the number of vowels in a given word

    >>> vowel_ctr('hello')
    2
    >>> vowel_ctr('mhmmm')
    0
    >>> vowel_ctr('')
    0
    >>> vowel_ctr('aadep')
    2
    >>> vowel_ctr('abaci')
    2
    >>> vowel_ctr('aalii')
    2
    '''
    count = 0 # intialize counter 
    vowels = ['a', 'e', 'i', 'o', 'u', 'y'] # make list with all the vowels 
    for vowel in vowels: # goes through word to see how many vowels from the list are in the word
        if vowel in word:
            count += 1 # counter will go up by one when it sees a vowel from the list in the word 
    return count # returns the count 
            



def report(word_ct, wordle_ct):
    '''
    reports the number of words in the file and the number of words that are good for wordle

    >>> report( 5, 10)
    The number of words is 5
    The number of good wordle words is 10
    
    '''
    print('The number of words is', word_ct) #prints the number of words in the file 
    print('The number of good wordle words is', wordle_ct) #prints the number of words that are good for wordle 

    return

def wordle_helper(fname, v_cutoff):
    '''
    Driver Function that takes the word document name and sorts how many words there are and how many words are good for wordle
    will call report function to do this
    '''
    myf = open(fname) #opens file 
    myf.readline() #reads lines of file 
    total_word_count = 0 #initialize a counter 
    for line in myf:
        total_word_count += 1

    myf = open(fname)
    myf.readline()
    total_good_wordle = 0 #initilize counter 
    print("Helpful Wordle Words:")  #print number of helpful wordle words
    for line in myf:
        if vowel_ctr(line) == v_cutoff:
            print(line.strip()) #strips the \n from word.text file)
            total_good_wordle += 1

    report(total_word_count, total_good_wordle) #call report fucnction to print numbers

    return 


    
def main():
    ''' wordle helper program driver'''
    wordle_helper('word.txt', 2)
    #wordle_helper('words.txt', 4)

    return

main()
       
    
print(doctest.testmod())    
    
    
    
    

