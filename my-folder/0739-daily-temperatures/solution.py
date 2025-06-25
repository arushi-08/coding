class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        
        # given array of int temp represents daily temp, return array answer such that answer[i] is number of days to wait after ith day to get a warmer temp

        # if no future day for which this is possible, keep answer[i] == 0

        #         2,1,1,0,0
        # 75,76

        # iterate from right
        # store idx of bigger elems, then add current idx

        i = len(temperatures)-2
        stack = [i+1]
        res = [0]
        while i >= 0:
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            
            if stack:
                res.append(stack[-1]-i)
            else:
                res.append(0)
            stack.append(i)
            i -= 1
        
        return res[::-1]
            

