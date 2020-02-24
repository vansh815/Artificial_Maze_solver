#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 04:15:42 2019

@author: vanshsmacpro
"""
from collections import deque
import sys
import json

# Parse the map from a given filename
def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().split("\n")]

# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
    
    return 0 <= pos[0] < n  and 0<= pos[1] < m 


def moves(map, row, col,directions_matrix):
    moves_possible = ((row+1,col), (row-1,col), (row,col-1), (row,col+1))
    
    filtered_move = []
    final_filtered = []
    for move in moves_possible:
        if(valid_index(move,len(map), len(map[1]))):
            filtered_move.append(move)
            
    for i in filtered_move:
        sx = 0
        sy = 0 
        (sx,sy) = i
        #print(sx,sy)
        if(map[sx][sy]=="." or map[sx][sy] == "@" and map[sx][sy]!="&"):
            final_filtered.append(i)
    for i in final_filtered:
        if (i[0] == row+1 and i[1] == col):
            directions_matrix[row+1][col]= directions_matrix[row][col] + "S"
        elif (i[0] == row-1 and i[1] == col):
            directions_matrix[row-1][col] = directions_matrix[row][col] + "N"
        elif (i[0] == row and i[1] == col+1):
            directions_matrix[row][col+1] = directions_matrix[row][col] + "E"
        elif (i[0] == row and i[1] == col-1):
            directions_matrix[row][col-1] = directions_matrix[row][col] + "W"
    #print(final_filtered)
    #when it backtrackes u have to create a condition such that if visited it does not backtrack !!!!!
    return final_filtered , directions_matrix
            
        #if valid_index(move, len(map), len(map[0])):
            #if map[move[0]][move[1]] == "." : 
         #       print(move)
          #      return move
            
    
    

def search1(IUB_map):
    # Find my start position
    you_loc=[(row_i,col_i) for col_i in range(len(IUB_map[0])) for row_i in range(len(IUB_map)) if IUB_map[row_i][col_i]=="#"][0]
    fringe= deque([(you_loc ,0)])
    boolean_matrix = []
    directions_matrix = []
    for i in range(len(IUB_map)):
        boolean_matrix.append([0]*len(IUB_map[0]))
    for i in range(len(IUB_map)):
        directions_matrix.append([-1]*len(IUB_map[0]))
    x1,y1 = (you_loc)
    directions_matrix[x1][y1] = ""
    
    while fringe:
        try:
            (curr_move, curr_dist)=fringe.popleft()
            (x,y) = curr_move
            if boolean_matrix[x][y] == 0:
                boolean_matrix[x][y] = 1
                number_moves , directions_matrix = moves(IUB_map, *curr_move,directions_matrix)
                for move in number_moves:
                    #print(move)
                    if IUB_map[move[0]][move[1]]=="@":
                        return curr_dist+1 , directions_matrix
                    else:
                        fringe.append((move, curr_dist + 1))
        except TypeError:
            print("infinte distance")
        #if (fringe == None):
            #if there exists no solution
         #   return -1 , -1
             
    
    

# Main Function
if __name__ == "__main__":
    IUB_map=parse_map(sys.argv[1])
    print("Shhhh... quiet while I navigate!")
    try:
        solution, directions_matrix = search1(IUB_map)
    #if((solution == -1) and (directions_matrix == -1)):
     #   print("Here's the solution i found" )
      #  print("Infinite")
    #else:
        dest_loc=[(row_i,col_i) for col_i in range(len(IUB_map[0])) for row_i in range(len(IUB_map)) if IUB_map[row_i][col_i]=="@"][0]
        #print("here is how you can reach that place")
        (dx , dy) = dest_loc
        print("Here's the solution I found:")
        print(solution,directions_matrix[dx][dy])
        
        
    except TypeError:
        print("Here the solution is :","Inf")
        
    