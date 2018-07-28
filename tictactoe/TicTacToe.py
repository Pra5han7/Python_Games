#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 15:21:32 2018

@author: prashant
"""
from boards import show_board,live_board
from win_lose_check import win
from flip_chance import flip
# Main program starts here
    #list of positions in the board. initially all blanks
#position=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
#list can also be defined as below
position=[' ']*9
print'*****welcome to TIC TAC TOE*****'
# player is a dictionary that have choices of the players either x or o
while True:
	
	player={'player1':None,'player2':None}
#get input from user for his choice x or o
	player['player1']=raw_input('player1 enter your choice X or O: ')

#if x chosen by player1 make player2 o or vice versa
	if player['player1']=='x':
    		player['player2']='o'
	else:
    		player['player2']='x'

#greet user with board help
    #===> a bug was here instead of chk_key key was used which was getting changed.
        # by the loop and greet was not able to address the correct player. 
        # used chk_key there and assigned the player value match to key.
	print'game is on {}'.format(player)
	for chk_key,value in player.items():
    		if value=='x':
        		key=chk_key
        		print'{} will go first'.format(key)
	show_board()


	for chance in range(9):
	    #pos is the response in number given by user
	    print'{}: enter your response where you want to mark'.format(key)
	    pos=input()
	    live_board(pos,key,position,player)      
        
	    res=win(key,position)
	    if (res):
		break
	    key=flip(key)
	if ' ' not in position or res==True:
		play_again=raw_input('want to play again. y/n: ')
		if play_again=='y':
			position=[' ']*9
		elif play_again=='n':
			print'*****THANKS FOR PLAYING*****'
			break
		else:
			print'not a valid choice. exiting*****'
