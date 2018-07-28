# show board to user
from __main__ import *


def show_board():
    print'board looks as below. use numbers to put your response'
    print'in the designated position\n'
    print'|7|8|9|'
    print'|4|5|6|'
    print'|1|2|3|'
    print'\n'

#live board with user responses
def live_board(num,key,position,player):
#    global position
    #check user dont select already filled position.
    if position[num-1] != ' ':
        num=input('position already marked. choose any vacant position: ')
        
    position[num-1]=player[key]
    print position
    i=8
    while i>=0:
        print'|{}|{}|{}|'.format(position[i-2],position[i-1],position[i])
        i-=3
