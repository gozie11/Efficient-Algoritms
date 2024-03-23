# I kinda cheesed this problem becasue the issuer expected a graph approach to be used...

def minOperations(arr):
  # Write your code here
  
  ops = 0 
  tracker = {num : idx for  idx, num in enumerate(arr)}
  for i in range(len(arr)):
    if arr[i] == i + 1:
      continue
    else:
      ops +=1
      stop = tracker[i+1] + 1 #input a number in the array and get the index back! More efficient that using arr.index(num)!
      arr[i:stop] = arr[i:stop][::-1]


  return ops


"""
Minimizing Permutations
In this problem, you are given an integer N, and a permutation, P of the integers from 1 to N, denoted as (a_1, a_2, ..., a_N). You want to rearrange the elements of the permutation into increasing order, repeatedly making the following operation:
Select a sub-portion of the permutation, (a_i, ..., a_j), and reverse its order.
Your goal is to compute the minimum number of such operations required to return the permutation to increasing order.
Signature
int minOperations(int[] arr)
Input
Array arr is a permutation of all integers from 1 to N, N is between 1 and 8
Output
An integer denoting the minimum number of operations required to arrange the permutation in increasing order
Example
If N = 3, and P = (3, 1, 2), we can do the following operations:
Select (1, 2) and reverse it: P = (3, 2, 1).
Select (3, 2, 1) and reverse it: P = (1, 2, 3).
output = 2
"""
