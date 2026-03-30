import copy
import random
from math import exp
import numpy as np
def make_board():
 rows, cols = (board_size, board_size)
 board=[]
 for i in range(rows):
  col=[]
  for j in range(cols):
   col.append("*")
  board.append(col)
 return board

def placeQueens(board):
 i=0
 while(i<board_size):
  row = random.randint(0, board_size-1)
  if board[row][i]!="Q":
   board[row][i]="Q"
   i+=1
 return board

def print_board(board):
 for i in range(board_size):
  for j in range(board_size):
   print(board[i][j], end=' ')
  print()

def getQueens(board, board_size):
 queen_positions=[]
 for i in range(board_size):
  for j in range(board_size):
   if board[i][j]=="Q":
    temp=i,j
    queen_positions.append(temp)
 return queen_positions

def make_chromosome(board):
 temp=[]
 for i in range(board_size):
  for j in range(board_size):
   if board[j][i]=="Q":
    temp.append(j)
 return temp

def generate_population(size):
 populat =[]
 for i in range(size):
  b = make_board()
  temp =placeQueens(b)
  temp2 = make_chromosome(temp)
  if temp2 not in populat:
   populat.append(temp2)
 return populat

import numpy.random as npr

def selectOne(fit):
 max=sum([c for c in fit])
 selection_probs=[c/max for c in fit]
 return fit.index(fit[npr.choice(len(fit), p=selection_probs)])

def selection(population, fit):
 new_p1 = copy.deepcopy(population)
 new_f1 = copy.deepcopy(fit)
 index1 = selectOne(new_p1)
 c1, f1=new_p1[index1], new_f1[index1]
 index2 = selectOne(new_p1)
 c2, f2=new_p1[index2], new_f1[index2]
 return c1, f1, c2, f2

def crossover(c1, c2):
 ra=np.random.randint(0,4)
 c3=c1[:ra]+c2[ra:]
 c4=c2[:ra]+c1[ra:]
 return c3, c4

def mutation(of_Spring, mutRate):
 for i in range(len(of_Spring)):
  if random.random() < mutRate:
   of_Spring[i] = random.randint(0, board_size - 1)
 return of_Spring

def Evaluate(of_Sp, Of_Fit, parent, p_fit):
 if Of_Fit >= p_fit:
  return of_Sp, Of_Fit
 else:
  return parent, p_fit

def objecive_function(board):
 queen_pos=getQueens(board, board_size)
 h_hit=0
 d_hit=0
 for i in range(0, len(queen_pos)):
  for j in range(i, len(queen_pos)):
   if i != j:
    if queen_pos[i][0]==queen_pos[j][0]:
     h_hit+=1
    if abs(queen_pos[i][0] - queen_pos[j][0]) == abs(queen_pos[i][1] - queen_pos[j][1]):
     print("queen_pos[i][0] - queen_pos[j][0]", queen_pos[i][0] , queen_pos[j][0])
     print("queen_pos[i][1] - queen_pos[j][1]", queen_pos[i][1], queen_pos[j][1])
     d_hit+=1
 return h_hit+d_hit

def main():
 global board_size
 board_size = int(input("Enter the board size: "))
 g = generate_population(board_size)
 print(g)
 board=make_board()
 print_board(board)
 placeQueens(board)
 print(getQueens(board, board_size))
 print_board(board)
 print("\nObjective Function", objecive_function(board))

if __name__=="__main__":
 main()
