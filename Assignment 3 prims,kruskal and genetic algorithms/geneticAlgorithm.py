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
 index1 = selectOne(new_f1)
 c1, f1=new_p1[index1], new_f1[index1]
 index2 = selectOne(new_f1)
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
     d_hit+=1
 return h_hit+d_hit

def fitness_from_chrom(chrom):
 attacks = 0
 n = len(chrom)
 for i in range(n):
  for j in range(i+1, n):
   if chrom[i] == chrom[j]:        
    attacks += 1
   if abs(chrom[i]-chrom[j]) == abs(i-j):   
    attacks += 1
 max_pairs = n*(n-1)//2
 return max_pairs - attacks          

def chrom_to_board(chrom):
 board = make_board()
 for col, row in enumerate(chrom):
  board[row][col] = "Q"
 return board

def run_ga():
 global board_size
 board_size = 8
 POP_SIZE      = 100
 MAX_GEN       = 500
 MUT_RATE      = 0.1
 perfect_score = board_size*(board_size-1)//2  

 print("="*55)
 print(f"  N-Queen GA Example   (board size = {board_size})")
 print("="*55)

 population = generate_population(POP_SIZE)
 print(f"\nStep 1 — Initial Population ({len(population)} chromosomes)")
 print("  First 4 chromosomes:")
 for ch in population[:4]:
  print("  ", ch)

 print("\nOne random board from the population:")
 print_board(chrom_to_board(population[0]))

 best_chrom  = None
 best_fit    = -1

 for gen in range(MAX_GEN):
  fit_scores = [fitness_from_chrom(c) for c in population]

  gen_best_fit   = max(fit_scores)
  gen_best_chrom = population[fit_scores.index(gen_best_fit)]

  if gen_best_fit > best_fit:
   best_fit   = gen_best_fit
   best_chrom = gen_best_chrom[:]


  if best_fit == perfect_score:
   print(f"\n  ✓  Perfect solution found at generation {gen}!")
   break

  new_population = []
  while len(new_population) < POP_SIZE:
   # Selection
   c1, f1, c2, f2 = selection(population, fit_scores)
   # Crossover
   c3, c4 = crossover(c1, c2)
   # Mutation
   c3 = mutation(c3, MUT_RATE)
   c4 = mutation(c4, MUT_RATE)
   # Evaluate
   c3, f3 = Evaluate(c3, fitness_from_chrom(c3), c1, f1)
   c4, f4 = Evaluate(c4, fitness_from_chrom(c4), c2, f2)
   new_population.extend([c3, c4])

  population = new_population[:POP_SIZE]

  if gen % 50 == 0:
   attacks = perfect_score - best_fit
   print(f"  Gen {gen:4d}  |  Best fitness: {best_fit}/{perfect_score}  |  Attacks: {attacks}")

 return gen

def run_10_times():
    results = []
    for i in range(10):
        gen_count = run_ga()  
        results.append(gen_count)
        print(f"Run {i+1:2d}: solved in {gen_count} generations")

    print(f"\nAverage generations: {sum(results)/len(results):.1f}")
    print(f"Min: {min(results)}  |  Max: {max(results)}")
    
if __name__ == "__main__":
 run_10_times()