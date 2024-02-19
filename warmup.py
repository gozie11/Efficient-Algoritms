"""
Find the probability that you get a hit on a battle ship map

"""
from typing import List
# Write any import statements here

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
  num_of_ones = 0
  result = 0.0
  divisor = len(G) * len(G[0])
  
  for row in G:
    for element in row:
      if element == 1:
        num_of_ones += 1
  result = num_of_ones / divisor
  return result
