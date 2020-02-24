
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 18:52:57 2019

@author: vanshsmacpro
"""

import sys
import datetime

# Parse the map from a given filename
def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().split("\n")]
    
def count_friends(board):
    return sum([ row.count('F') for row in board ] )

def printable_board(board):
    return "\n".join([ "".join(row) for row in board])

def add_friend(board, row, col):
    return board[0:row] + [board[row][0:col] + ['F',] + board[row][col+1:]] + board[row+1:]

def valid_move(board,r,c):
    pos_building_x = []
    pos_building_y = []
    position_friend_x = []
    position_friend_y = []
    count_x = 0
    count_y = 0 
    flag_right = 0
    flag_left = 0 
    flag_up = 0 
    flag_down = 0 
    
    #to check the left side of the column 
    
    for i in range(len(board[0])):
        if(board[r][i] =="F"):
            count_x = count_x + 1
            
        
    for i in range(len(board)):
        if(board[i][c] =="F"):
            count_y = count_y + 1
    if(count_x>0 or count_y > 0):
        for i in range(len(board[0])):
            if(board[r][i]== "&"):
                pos_building_x.append(i)
                
           
        for i in range(len(board)):
            if(board[i][c]== "&"):
                pos_building_y.append(i)
        
        for i in range(len(board[0])):
            if(board[r][i] == "F"):
               position_friend_x.append(i)
        
        for i in range(len(board)):
            if(board[i][c]== "F"):
                position_friend_y.append(i)
    else:
        return 1
    
    if(count_x > 0 and len(pos_building_x)==0):
        return 0 
    if(count_y > 0 and len(pos_building_y)==0):
        return 0 
    # for right side of my position
    # my position
    # nearest &
    # nearet F
    building_right = []
    friend_right = []
    for i in pos_building_x:
        if(c<i):
            building_right.append(i)
    for i in position_friend_x:
        if(c<i):
            friend_right.append(i)
    if(len(building_right)==0 and len(friend_right)!=0):
        flag_right = 0
    elif(len(building_right)==0 and len(friend_right)==0):
        flag_right = 1
    elif(len(building_right)!=0 and len(friend_right)==0):
        flag_right = 1
    elif(len(building_right)!=0 and len(friend_right)!=0):
        b_r = min(building_right)
        f_r = min(friend_right)
        if(c < b_r < f_r):
            flag_right = 1
        else:
            flag_right = 0
   
    # to check the left side of my position
    building_left = []
    friend_left = []
    for i in pos_building_x:
        if(i<c):
            building_left.append(i)
    for i in position_friend_x:
        if(i<c):
            friend_left.append(i)
    if(len(building_left)==0 and len(friend_left)!=0):
        flag_left = 0
    elif(len(building_left)==0 and len(friend_left)==0):
        flag_left = 1
    elif(len(building_left)!=0 and len(friend_left)==0):
        flag_left = 1
    elif(len(building_left)!=0 and len(friend_left)!=0):
        b_l = max(building_left)
        f_l = max(friend_left)
        if(f_l < b_l < c):
            flag_left = 1
        else:
            flag_left = 0
    # to check the upper side 
    
    building_up = []
    friend_up = []
    for i in pos_building_y:
        if(i<r):
            building_up.append(i)
    for i in position_friend_y:
        if(i<r):
            friend_up.append(i)
    if(len(building_up)==0 and len(friend_up)!=0):
        flag_up = 0
    elif(len(building_up)==0 and len(friend_up)==0):
        flag_up = 1
    elif(len(building_up)!=0 and len(friend_up)==0):
        flag_up = 1
    elif(len(building_up)!=0 and len(friend_up)!=0):
        b_u = max(building_up)
        f_u = max(friend_up)
        if(f_u < b_u < r):
            flag_up = 1
        else:
            flag_up = 0
    # to check the down side 
    building_down = []
    friend_down = []
    for i in pos_building_y:
        if(r<i):
            building_down.append(i)
    for i in position_friend_y:
        if(r<i):
            friend_down.append(i)
    if(len(building_down)==0 and len(friend_down)!=0):
        flag_down = 0
    elif(len(building_down)==0 and len(friend_down)==0):
        flag_down = 1
    elif(len(building_down)!=0 and len(friend_down)==0):
        flag_down = 1
    elif(len(building_down)!=0 and len(friend_down)!=0):
        b_d = min(building_down)
        f_d = min(friend_down)
        if(c < b_d < f_d):
            flag_down = 1
        else:
            flag_down = 0
            
    
        
    if(flag_right == 1 and flag_left == 1 and flag_up == 1 and flag_down == 1):
        return 1 
    else:
        return 0 

def successors(board, successors_list):
    
    matrix = []
    for r in range(0, len(board)):
        for c in range(0,len(board[0])) :
            if (board[r][c] == '.') and (valid_move(board,r,c)== 1):
                board_new = add_friend(board, r,c)
                
                if successors_list.count(board_new) == 0:
                    matrix.append(board_new)
                    successors_list.append(board_new)
    #print(matrix)
    return matrix
                  
        

# check if board is a goal state
def is_goal(board):
    return count_friends(board) == K 

# Solve n-rooks!
def solve(initial_board):
    successors_list = []
    fringe = [initial_board]
    #print(len(fringe))
    while len(fringe) > 0:
        for s in successors( fringe.pop(), successors_list ):
            if is_goal(s):
                return(s)
            fringe.append(s)
            
    return False

if __name__ == "__main__":
    IUB_map=parse_map(sys.argv[1])

    # This is K, the number of friends
    K = int(sys.argv[2])
    print ("Starting from initial board:\n" + printable_board(IUB_map) + "\n\nLooking for solution...\n")
    first = datetime.datetime.now()
    solution = solve(IUB_map)
    print(str(datetime.datetime.now() - first) + "\n")
    print ("Here's what we found:")
    print (printable_board(solution) if solution else "None")
# check if board is a goal state

