class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        
        ans = []
        for i in range(numRows):
            if i == 0:
                ans.append([1])
            else:
                temp = [1]
                for k in range(1, i):
                    temp.append(int(self.factorial(i)/(self.factorial(i-k)* self.factorial(k))))
                temp.append(1)
                ans.append(temp)
        
        return ans
    
    def factorial(self,n):
        
        if n <= 1:
            return 1
        
        return self.factorial(n-1) * n
        
        
