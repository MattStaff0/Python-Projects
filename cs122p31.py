'''Hello Pyhton, Part 1
Author:Matthew Stafford, C. Science
Credit: CS122 resources only
Description: Using turtle grpahics to draw a house and polygons at certain positon

'''
from turtle import*

def poly(num_sides, side_len, pcolor):
    '''
    Drawing a polygon
    '''
    fillcolor(pcolor)
    begin_fill()
    for i in range(num_sides):
        fd(side_len)
        lt(360 / num_sides)
    end_fill()
    
    return

def jump(x,y):
    '''
    aux function sets turtle position
    without leaving pen trail
    >>> jump(100, 100)
    [turtle positioned at 100, 100]
    '''
    up()
    goto(x,y)
    down()

    return

def house():
    ''' Runs code to draw the house at a certian location'''
    house_color = "green"
    roof_color = "yellow"
    x = 0
    y = 100
    poly(4, 100, house_color)
    jump(0,100)
    poly(3, 100, roof_color)

    return
    

def main():
    ''' driver for code to draw a house'''
    title("A Very Fine House")
    speed(0)
    hideturtle()
    house()

    return

main()







