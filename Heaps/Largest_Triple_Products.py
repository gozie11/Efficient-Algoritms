import math

def findMaxProduct(arr):
  # Write your code here
  import heapq # Major key
  #heappush(list, int) , heappop(list)
  res = []
  heap = []
  for i in range(len(arr)):
    heapq.heappush(heap, arr[i])
    if i < 2: 
      res.append(-1)
      continue
    if len(heap) > 3 :
      #the pop will remove the smallest element from the heap, naturally leaving us with the greatest 3 elements.
      heapq.heappop(heap)
      prod = heap[0] * heap[1] * heap[2]

    else:
      
      prod = heap[0] * heap[1] * heap[2]
        
    res.append(prod)
  return res



def findMaxProduct(arr):
  
  # my first attempt is a pretty slow O(n^2 log n) approach
  
  # Write your code here
  
  res = []

  for i in range(len(arr)):
    if i < 2: res.append(-1)
    
    else:
      #take a splice of the input to find the max the values from
      sample = arr[0:i+1:]

      # we can sort it to easily grab maxes
      sample.sort()
      
      prod = 1
      # the final greatest 3 elements will always be in the last 3 positions of the array i.e. [len(arr)-3::] 
      final = sample[(len(sample)-3)::1]
      
      for element in final:
        prod *= element
        
      res.append(prod)
  return res









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
  arr_1 = [1, 2, 3, 4, 5]
  expected_1 = [-1, -1, 6, 24, 60]
  output_1 = findMaxProduct(arr_1)
  check(expected_1, output_1)

  arr_2 = [2, 4, 7, 1, 5, 3]
  expected_2 = [-1, -1, 56, 56, 140, 140]
  output_2 = findMaxProduct(arr_2)
  check(expected_2, output_2)


  # Add your own test cases here
  
