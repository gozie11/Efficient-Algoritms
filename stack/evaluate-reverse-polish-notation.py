#learned this solution from cornElius in technical 2025 slack chanel

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        """

        good space for tracing problems etc

        """

        op={
            "+": lambda a,b: a+b,
            "-": lambda a,b: a-b,
            "*": lambda a,b: a*b,
            "/": lambda a,b: int(a/b)
        }

        stack = []

        for token in tokens:


            # stack.append(op[token](fst,sec)) 


            if token in op:
                fst = stack.pop()
                sec = stack.pop()
                operation = op[token]
                val=operation(sec,fst) # This piece caught me off guard . second must come first because it's reverse polish notation
                stack.append(val) 

            else:
                stack.append(int(token))

        return stack.pop()
