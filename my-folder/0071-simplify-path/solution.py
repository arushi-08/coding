import re
class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []
        dots = 0
        dirname = ''

        for i in path+'/':

            if i == '.':
                dots += 1

            if i == '/':
                if set(dirname) == set('.'):
                    if dots == 2:
                        if stack:
                            stack.pop()
                    elif dots > 2:
                        stack.append('.'*dots)
                
                elif dirname:
                    stack.append(dirname)

                dirname = ''
                dots = 0

            else:
                dirname += i

        return '/'+ '/'.join(stack)
