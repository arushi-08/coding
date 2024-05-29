class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []
        comb = {'2':['a','b','c'], 
        '3':['d','e','f'], '4':['g','h','i'],
        '5':['j','k','l'], '6':['m','n','o'],
        '7':['p','q','r','s'], '8':['t','u','v'],
        '9':['w','x','y','z']}
        ans = []
        def backtrack(res, index):
            if index == len(digits):
                ans.append("".join(res))
                return
            
            
            for j in range(len(comb[digits[index]])):
                res.append(comb[digits[index]][j])
                backtrack(res, index + 1)
                res.pop()
        
        backtrack([], 0)
        return ans
