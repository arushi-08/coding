class Solution:
    def simplifyPath(self, path: str) -> str:
        
        # use stack to pop folders before '..'
        # reset the curr_path
        # for loop add '/' to path: path + '/'

        stack = []
        curr_path = ''
        # /home/
        for c in path + '/':

            if c == '/':
                if curr_path == '..':
                    if stack:
                        stack.pop()
                
                elif curr_path != '' and curr_path != '.':
                    stack.append(curr_path)
                curr_path = ''

            else:
                curr_path += c
        
        return '/' + '/'.join(stack)
