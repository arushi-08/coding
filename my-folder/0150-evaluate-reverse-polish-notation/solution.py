class Solution:
    def add(self, x, y): return x + y
    def subtract(self, x, y): return x - y
    def multiply(self, x, y): return x * y
    def divide(self, x, y): return int(x / y)

    def evalRPN(self, tokens: List[str]) -> int:

        # put numbers in stack till operator, 
        # 2 , 1 + then you pop numbers from stack and do operation put back in stack
        # next operation

        stack = []
        operations = ['+', '-', '*', '/']
        for i in range(len(tokens)):
            if tokens[i] not in operations:
                stack.append(int(tokens[i]))
            else:
                y, x = stack.pop(), stack.pop()
                if tokens[i] == '+':
                    ans = self.add(x, y)
                elif tokens[i] == '-':
                    ans = self.subtract(x, y)
                elif tokens[i] == '*':
                    ans = self.multiply(x, y)
                else:
                    ans = self.divide(x, y)
                stack.append(ans)
        
        return stack.pop()

