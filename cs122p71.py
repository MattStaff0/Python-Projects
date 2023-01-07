'''In the loop (dna to rna transcription)
Author:Matthew Stafford, C. Science
Credit: CS122 resources only
Description: Writing a program that decodes dna into rna strands
'''

import doctest

def transcribe1(s):
    '''
    (s: str) -> str

    Return a transcribed verson of S which ignores all letters besides
    A, C, G, T

    >>> transcribe1('ACGT TGCA')
    'UGCAACGU'
    >>> transcribe1('GATTACA')
    'CUAAUGU'
    >>> transcribe1('GAtTtTACA')
    'CUAAUGU'
    >>> transcribe1('TTt ACT')
    'AAUGA'
    >>> transcribe1('cs5')
    ''
    '''
    
    d = ''     #defining an empty string to print the transcription
    for letters in s:  # for loop will go through every letter in 's'
        if letters == 'A':
            a = 'U'
        elif letters == 'C':
            a = 'G'
        elif letters == 'G':
            a = 'C'
        elif letters == 'T':
            a = 'A'
        else:  # makes sure only the letters we want will get transcribed 
            a = ''
            
        d += a #adds a to final translation 

    return d 
        
    
#Part 2 using a while loop
        


def transcribe2(s):
    '''
    (s: str) -> str

    Return a transcribed verson of S which ignores all letters besides
    A, C, G, T

    >>> transcribe1('ACGT TGCA')
    'UGCAACGU'
    >>> transcribe1('GATTACA')
    'CUAAUGU'
    >>> transcribe1('GAtTtTACA')
    'CUAAUGU'
    >>> transcribe1('TTt ACT')
    'AAUGA'
    >>> transcribe1('cs5')
    ''
    '''

    d = '' # making a counter variable and an empty string for while loop
    counter = 0

    while counter < len(s):
        if s[counter] == 'A':
            a = 'U'
        elif s[counter] == 'C':
            a = 'G'
        elif s[counter] == 'G':
            a = 'C'
        elif s[counter] == 'T':
            a = 'A'
        else:  # makes sure only the letters we want will get transcribed 
            a = ''

        counter += 1 # used to add 1 to the counter for the while loop
        d += a #adds a to final translation

        return d # returns value of d for other functions
    
    
# doctest
print(doctest.testmod())


        
    
    









