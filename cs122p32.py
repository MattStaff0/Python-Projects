'''CS 122 Fall 2022 Project 3-2
Author(s): Matthew Stafford
Credit: CS 122 Resources only
Description: Intro to turtle graphics drawing a star
'''

from turtle import*

def jump(x, y):
    '''aux function sets turtle position without leaving pen trail

>>> jump(100, 100)
 [turtle positioned at 100, 100]
 '''
    penup()
    setposition(x, y)
    pendown()

    return

def main():
    '''driver for code to draw a sun'''

    # set up turtle environment
    reset()
    title('Closest Star')
    speed('fastest')
    hideturtle()

    # draw the sun
    #sunshine(0, 0)

    return

def sunshine():
    '''starts the drawing of the sun labeled as the Closest Star'''
    main()
   
    color('yellow')
    width('0.75')
   
    for i in range(175):
        forward(175)
        lt(3)
        jump(0,0)
    '''code to draw the star 
    >>>sunshine()'''

    return
