class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for i in range(len(tokens)):
            if tokens[i].lstrip("-").isdigit():
                stack.append(int(tokens[i]))
            else:
                # print(stack)
                b = stack.pop()
                a = stack.pop()
                # print(a,b, tokens[i])
                if tokens[i] == '+':
                    stack.append(a+b)
                elif tokens[i] == '*':
                    stack.append(a*b)
                elif tokens[i] == '-':
                    stack.append(a-b)
                else:
                    stack.append(int(float(a)/b))
                # print(stack)
        return stack.pop()
