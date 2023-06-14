class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
#         1, 11 1C0 1C1, 121, 2C0 2C1 2C2 121, 3C0 3C1 3C2 3C3
        def fact(x):
            if x == 0 or x == 1: return 1
            # print('here',x, fact(x-1)*x)
            return fact(x-1)*x
        
        def comb(i, j):
            # print('c',i, j, fact(i))
            return int(fact(i)/(fact(j)*fact(i-j)))
        
        ans = []
        for i in range(numRows):
            temp = []
            if i == 0:
                ans.append([1])
                continue
            for j in range(i+1):
                temp.append(comb(i,j))
            ans.append(temp)
            # break
            # break
        return ans
