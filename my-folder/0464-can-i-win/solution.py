class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        
        # each player will choose max number
        # try to subtract the max choosable int from desired total

        if desiredTotal <= 0:
            return True

        if (maxChoosableInteger * (maxChoosableInteger + 1)) // 2 < desiredTotal:
            return False

        self.memo = {}

        def helper(desiredTotal, choices):
            
            if choices and choices[-1] >= desiredTotal:
                return True

            choice_tuple = tuple(choices)
            if choice_tuple in self.memo:
                return self.memo[choice_tuple]
                
            for i in range(len(choices)):

                choices_next = choices[:i] + choices[i+1:]
                if not helper(desiredTotal-choices[i], choices_next):
                    self.memo[choice_tuple] = True
                    return True
                    
            self.memo[choice_tuple] = False
            return False
        
        ans = helper(desiredTotal, list(range(1, maxChoosableInteger+1)))

        return ans

    
