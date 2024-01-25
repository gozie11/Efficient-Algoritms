#this is my first attemt. I'm getting an error for trying to pop from an empty list. I will return to trace this tomorrow and figure out the bug.

class Solution:
    
    def operatorHelper(self, operator:str, first_digit:int, second_digit:int ) -> int:
        result = 0 
        if operator == "+":
            result = first_digit + second_digit
        if operator == "-":
            result = first_digit - second_digit
        if operator == "*":
            result = first_digit * second_digit
        if operator == "/":
            # this section is hacky. We need to check if the absolute values 
            # are acceptable for integer division in order to get the desired output.
            # e.g. 6/-132 wouldn't return 0. It would return -1 using integer division (//). 

            if abs(first_digit) < abs(second_digit): return 0
            result = first_digit // second_digit
        return result

    #the python isdigit function is not recognizing negative numbers so I'm tweaking the function. 
    def is_digit(self, digit:str):
        try:
            int(digit)
            return True
        except ValueError:
            return False

    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1: return int(tokens[0])
        #integer stack
        operands = []
        #operators = []

        for value in tokens:
            #this is digit function is not accounting for the negative -11
            if self.is_digit(value):

                operands.append(int(value))

            else:
                print("operator ", value)
                print(operands)
                second_digit = operands.pop()
                print("second_digit",second_digit)
                first_digit = operands.pop()
                print("first_digit",first_digit)

                result = self.operatorHelper(value, first_digit, second_digit)
                operands.append(result)
                print(operands)

        result = operands.pop()
        return result

           

                result = self.operatorHelper(value, first_digit, second_digit)
                operands.append(result)
                print(operands)

        result = operands.pop()
        return result

           
