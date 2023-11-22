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
            result = first_digit // second_digit
        return result

    def evalRPN(self, tokens: List[str]) -> int:
        #integer stack
        operands = []
        #operators = []

        for value in tokens:
            
            if value.isdigit():
                operands.append(int(value))
            else:
                print(operands)
                second_digit = operands.pop()
                first_digit = operands.pop()
                result = self.operatorHelper(value, first_digit, second_digit)
                operands.append(result)
                print(operands)

        result = operands.pop()
        return result

           
