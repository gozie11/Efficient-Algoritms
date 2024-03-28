import math


def minOverallAwkwardness(arr):
# Write your code here

  A = []
  B = []
  arr.sort()
  for i in range(0, len(arr), 2):
      A.append(arr[i])
      B.append(arr[i+1]) if i + 1 < len(arr) else None

  # how could I optimize this check?
  top = max(
    abs(A[-1] - B[-1]) , 
    abs(A[0] - B[0]) , 
    abs(A[-1] - A[-2]) , 
    abs(B[-1] - B[-2]) , 
    abs(A[0] - A[1]), 
    abs(B[0] - B[1])
  )

  return (top)
