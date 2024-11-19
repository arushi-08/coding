class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        # replace every number
        # if k > 0 
        # replace ith with sum of next k numbers
        # if k < 0
        # replace ith with sum of previous k numbers
        # if k == 0, i = 0

        n = len(code)
        code_new = code.copy()

        if k > 0:
            for i in range(n):
                new_val = 0
                for j in range(i+1, min(n, i+k+1)):
                    new_val += code[j]

                if n < (i+k+1):
                    for j in range(i + k + 1 - n):
                        new_val += code[j]

                code_new[i] = new_val
        elif k < 0:
            for i in range(n):
                new_val = 0
                print('i', i)
                if i != 0:
                    for j in range(max(0,i-1), max(-1, i+k-1),-1):
                        # print('j', j)
                        new_val += code[j]
                print(i, new_val)
                covered = i
                print('covered', covered, n + k + covered-1)
                if 0 > i + k - 1:
                    for j in range(n-1, n + k + covered-1,-1):
                        print('inside',i, code[j])
                        new_val += code[j]
                # print('out', i, new_val)
                code_new[i] = new_val
        else:
            return [0] * len(code)
        
        return code_new
                



        

