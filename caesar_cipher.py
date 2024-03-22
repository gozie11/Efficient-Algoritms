# This template was not though of by me! Neither were the tests... don't sue me.

import math
# Add any extra import statements you may need here


# Add any helper functions you may need here
def rotate(char, r_f):
  if char.isdigit():
    return chr(    (ord(char) + r_f - ord('0')) % 10 + ord('0')  ) 
  elif char.islower():
    return chr(    (ord(char) + r_f - ord('a')) % 26 + ord('a')  ) 
  else:
    return chr(    (ord(char) + r_f - ord('A')) % 26 + ord('A')  ) 

  
def rotationalCipher(input_str, rotation_factor):
  # Write your code here
  if not input_str or not rotation_factor: return input_str
  res = ""  
  for char in input_str:
    if char.isalnum():
      res += rotate(char,rotation_factor)      
    else: res += char
    
  return res


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printString(string):
  print('[\"', string, '\"]', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  input_1 = "All-convoYs-9-be:Alert1."
  rotation_factor_1 = 4
  expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
  output_1 = rotationalCipher(input_1, rotation_factor_1)
  check(expected_1, output_1)

  input_2 = "abcdZXYzxy-999.@"
  rotation_factor_2 = 200
  expected_2 = "stuvRPQrpq-999.@"
  output_2 = rotationalCipher(input_2, rotation_factor_2)
  check(expected_2, output_2)

  # Add your own test cases here
  
