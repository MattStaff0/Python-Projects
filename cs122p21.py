'''Form and Function, Part 1 (Bridges)
Author:Matthew Stafford, C. Science
Credit: None
Description: Writing code to see the maximum weight that can be transported along the road'''

def max_trans1(a, b, c):
    '''Function that prints the maximum weight that can be transported along the 3 bridges'''
    print('The maximum weight that can be transported is:', min(a, b, c))
    return

def max_trans2(a, b, c, d, e):
    '''Function that prints the maximum weight that can be transported along all 5 bridges'''
    maximum_route_1 = min(a, b, c)
    maximum_route_2 = min(d, e)
    print('The maximum weight that can be transported across all 5 bridges is', max(maximum_route_1, maximum_route_2))
    return





