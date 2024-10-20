class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        
        # evaluate inner expression
        # go till the innermost
        # encounter open bracket put items in stack
        # encounter close bracket
        # keep popping till open bracket found
        # look at its left instruction evaluate that

        stack = []

        for i in range(len(expression)):
            if expression[i] != ')':
                stack.append(expression[i])
            else:
                evals = []
                while stack[-1] != '(':
                    evals.append(stack.pop())
                
                if stack[-1] == '(':
                    stack.pop()

                if stack[-1] == '&':
                    result = True
                    for i in evals:
                        if i in ['f',False]:
                            result = False
                            break
                    stack.pop()
                
                elif stack[-1] == '|':
                    result = False
                    for i in evals:
                        if i in ['t',True]:
                            result = True
                            break
                    stack.pop()
                
                elif stack[-1] == '!':
                    if evals[-1] in ['f',False]:
                        result = True
                    else:
                        result = False
                stack.append(result)
        
        print(stack)
        return stack[-1]
            

