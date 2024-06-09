class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        
        i = 0
        reverse = False
        forward = True
        while True:
            if forward and k > 0 and i < n-1:
                k -= 1
                i += 1
                if i == n-1:
                    reverse = True
                    forward = False
            
            if k == 0:
                return i
            
            if reverse and k > 0 and i > 0:
                k -= 1
                i -= 1
                if i == 0:
                    forward = True
                    reverse = False
            if k == 0:
                return i
        
        
