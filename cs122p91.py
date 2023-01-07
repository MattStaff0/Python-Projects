''' Mars Data Analysis 
Authors:Matthew Stafford, Michael Duffy, C. Science
Credit: CS122 resources only
Description: Writing a program that uses turtle grpahics to get points of info and analzying that data
for mean mode and range
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
                                   
    x = rover_loc()
    y = rover_loc()
    goto(x, y)
    stamp()
    water = water_content()
    temp = temperature()
    
    print(x, '\t',  
          y, '\t',
          water, '\t',
          temp, '\t')
          
    return water, temp # return water and temp 


def analyze_data(li):
    ''' analyze data to calculate the mean, mode, and range if data is empty the mode value
        should be set to 0
        >>> analyze_data([100, 100, 200])
        (133.33, [100], (100, 200))
        >>> analyze_data([-150, 0])
        (-75, [], (-150, 0)) '''
    mean = round(statistics.mean(li), 2)     #make mean variable and have it round to 2 decimal points 
    mode = [statistics.mode(li)]    # make mode variable using stats
    Range = (min(li), max(li))      # take the min and max of li to find rnage values 

    return mean, mode, Range


def mars_report(dtype, dmean, dmode, drange):
    '''
    fucntion that prints the analzyed data, pritns out the header, the mean, mode and range for both
    the water values and the temperatrue values
    >>> mars_report('Water', wmean, wmode, wrange)
    Water Content Data Analysis 
    range: 12 to 260 
    mean: 138.65 
    mode: [184]
    '''
    print(dtype,'Content Data Analysis','\n', # printing the header of the data anaylsis 
          'range:', drange[0], 'to', drange[1], '\n',   #print  range
          'mean:', dmean)
    if dmode == []: #seeing if dmode is equal to an empty list or not 
        print('no value occured more than one time')
    else: #if not an empty list print normally 
        print(' mode:', dmode)
                    
    return   
    

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
    water = []  #making empty list for water value
    temp = []   
    for i in range(n):
        w, t = collect_data()  # making w and t equal to collect_data to be able to append values to lists
        water.append(w) #adding the value of w to empty list 
        temp.append(t)  
    wmean, wmode, wrange = analyze_data(water) #
    tmean, tmode, trange = analyze_data(temp)
    mars_report('Water', wmean, wmode, wrange) 
    mars_report('Temperature', tmean, tmode, trange)
        

    return

def mars_explore_main():
    '''main function for mars_explore'''
    mars_explore_setup()
    pass
    mars_explore(20)
    return


mars_explore_main()











