# check for win
from __main__ import *
def win(key,position):
    # case1=> horizontal alignment
    #===> a bug was here I used for i in range(3) and incremented i by three. 
        # it doesnt work i will always iterate range. used while after that
    i=0
    while (i<=6):
        if position[i]==position[i+1] and position[i]==position[i+2] and position[i] != ' ':
          # uncomment below line for debugging win cases 
            # print'inside 1st for loop'
            print '{} won'.format(key)
            print'*****Horizontal alignment*****'
            return True
        i+=3
     # case 2=> vertical alignment
    for i in range(3):
        if position[i]==position[i+3] and position[i]==position[i+6] and position[i] != ' ':
            # uncomment below line for debugging win cases 
            #print'inside 2nd for loop'
            print '{} won'.format(key)
            print'*****Vertical alignment*****'
            return True
    # case 3=> diagonal alignment
    #position[::4] checks for 0,4,8 and position[2:7:2] for2,4,6 positions not to be blank
    #refer slicing for more info
    if position[0]==position[4] and position[0]==position[8] and position[::4] !=[' ',' ',' ']:
       # uncomment below line for debugging win cases 
        #print'inside 1st diagonal case'
        print '{} won'.format(key)
        print'*****Diagonal alignment*****'
        return True
            
    if position[2]==position[4] and position[2]==position[6] and position[2:7:2] !=[' ',' ',' ']:
        # uncomment below line for debugging win cases 
        #print'inside 2nd diagonal case'
        print '{} won'.format(key)
        print'*****Diagonal alignment*****'
        return True
    if ' ' not in position:
        print'\n*****Its a draw*****'
