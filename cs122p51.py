'''Mars Rover
Author:Matthew Stafford, C. Science
Credit: CS122 resources only
Description: Writing a program that uses turtle grpahics to get points of info
'''

from turtle import*
import random
import statistics 

def rover_loc():
    '''
    return random number for rover location
    >>> rover_loc()
    125 [for example]
    '''
    return random.randint(-275, 275)

def water_content():
    '''
    return random number for water amount
    >>> water_content()
    239 [example]
    '''
    return random.randint(1, 290)


def temperature():
    '''
    return random number for temperature
    >>> temperature()
    -100 [example]
    '''
    return random.randint(-178, 1)


def collect_data():
    '''Collect data and sets up table
    >>>collect_data()
    xpos    ypos    water   temp'''
    data_collect = {}           # made tuple with data_collect{} 
    data_collect[1] = rover_loc() #made tuples replacing the origonal variables 
    data_collect[2] = rover_loc() 
    goto(data_collect[1], data_collect[2])
    stamp()
    data_collect[3] = water_content()
    data_collect[4] = temperature()
    '''
    x = rover_loc()
    y = rover_loc()
    goto(x, y)
    stamp()
    water = water_content()
    temp = temperature()
    '''
    print(data_collect[1], '\t',  # print each tuple 
          data_collect[2], '\t',
          data_collect[3], '\t',
          data_collect[4], '\t')

    return

def analyze_data(li):
    ''' analyze data to calculate the mean, mode, and range if data is empty the mode value
        should be set to 0
        >>> analyze_data([100, 100, 200])
        (133.33, [100], (100, 200))
        >>> analyze_data([-150, 0])
        (-75, [], (-150, 0)) '''
    mean = sorted(statisitcs.mean(li))
    
    

def mars_explore_setup():
    '''
set up printed and graphical output called from: mars_explore_main
>>> mars_explore_setup()
'''
# print title line for printed output
    print('xpos', '\t',
          'ypos', '\t',
          'water', '\t',
          'temp')
    reset()
    title('Mars Rover')
    speed('fastest')
    display_color = 'blue'
    pencolor(display_color)
    dot(10, display_color)
    
    return


def mars_explore(n):
    '''run collect data for how many times needed
        >>> mars_explore()
        xpos    ypos    water   temp
        118     88      203     -5
        '''
    for i in range(n):
        collect_data()

    return

def mars_explore_main():
    '''main function for mars_explore'''
    mars_explore_setup()
    pass
    mars_explore(20)
    return


mars_explore_main()











