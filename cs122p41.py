'''Safe Lead
Author:Matthew Stafford, C. Science
Credit: CS122 resources only
Description: Determine if a lead in a basketball game is safe
'''

def safe_lead(lead, possession, time):
    '''
    function that takes the lead of one team and subtracts by 3
    then sees which team has possession of the ball
    then squares the lead and chekcs if the lead is greater or less than the time
    >>>safe_lead(20, True, 5)
    This is a safe lead!
    '''
    lead = lead - 3
    if possession == True:
        lead += .5
    else:
        lead -= .5
    lead = lead ** 2
    if lead > time:
        print("This is a safe lead!")
    else:
        print("This is not a safe lead!")

    return

def main():
    '''
    main fucntion that takes input then prints safe_lead
    '''
    
    lead = input("What is the lead of the game: ")
    lead = int(lead)
    
    possession = input("Who has possession of the game:(Using True and False): ")
    possession = bool(possession)
    
    time = input("How much time is left in the game: ")
    time = int(time)
    
    safe_lead(lead, possession, time)

    return
    

main()

        
        
   
    
