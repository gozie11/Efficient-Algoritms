# I didn't create this question don't sue me. I did write the algo out though.

import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def count_subarrays(arr):
  # Write your code here
  #this is going to be a monotonic stack solution
  n = len(arr)
  
  if n == 1 : return [1]
  
  # 2 arrays that will be used to track the number of subarrays that satisfy the condidtions to the left and to the right of i respectively
  # the arrays are being initialized with their worst case results
  left = [i+1 for i in range(n)]
  
  right = [n - i for i in range(n)]
  
  stack = []

  
  # calculate the left ward elements that i is greater than
  for i in range(n):
    while stack and arr[stack[-1]] < arr[i]:
      stack.pop()
    left[i] = i + 1 if not stack else  i - stack[-1] # why would this be i - stack[-1] ..becasue the first thing we can subtract is 0 
    stack.append(i)
    
  
  stack.clear()
  
  for i in range(n-1,-1,-1):
    while stack and arr[stack[-1]] < arr[i]:
      stack.pop()
      
    right[i] = n - i if not stack else stack[-1] - i
    stack.append(i)
  
  result = [left[i] + right[i] - 1 for i in range(n)]
  
  return result









# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

def printIntegerList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
    if i != 0:
      print(', ', end='')
    print(array[i], end='')
  print(']', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
    result = False
  for i in range(min(expected_size, output_size)):
    result &= (output[i] == expected[i])
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printIntegerList(expected)
    print(' Your output: ', end='')
    printIntegerList(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  test_1 = [3, 4, 1, 6, 2]
  expected_1 = [1, 3, 1, 5, 1]
  output_1 = count_subarrays(test_1)
  check(expected_1, output_1)
  
  test_2 = [2, 4, 7, 1, 5, 3]
  expected_2 = [1, 2, 6, 1, 3, 1]
  output_2 = count_subarrays(test_2)
  check(expected_2, output_2)

  # Add your own test cases here
  
