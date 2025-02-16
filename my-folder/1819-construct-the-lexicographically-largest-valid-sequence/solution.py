class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        
        if n==1: return [1]

        ans = [0] * (2*n-1)
        ans[0], ans[n] = n, n
        used = [False] * (n+1)
        used[0], used[n] = True, True

        self.helper(ans, 1, used, n)
        
        return ans
    
    def helper(self, ans, j, used, n):

        if j == len(ans):
            return True

        if ans[j] != 0:
            return self.helper(ans, j+1, used, n)

        for i in range(n-1,0,-1):
            if not used[i]:
                if i == 1:
                    ans[j] = i
                    used[i] = True
                    if self.helper(ans, j+1, used, n):
                        return True

                    used[i] = False
                    ans[j] = 0
                else:
                    if j+i < len(ans) and ans[j+i] == 0:
                        ans[j+i] = i
                    else:
                        continue
                
                    ans[j] = i
                    used[i] = True
                    if self.helper(ans, j+1, used, n):
                        return True
                    ans[j] = 0
                    used[i] = False
                    ans[j+i] = 0

        return False
         

