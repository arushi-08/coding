class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        mapping = {"2":"abc",
                   "3":"def",
                   "4":"ghi",
                   "5":"jkl",
                   "6":"mno",
                   "7":"pqrs",
                   "8":"tuv",
                   "9":"wxyz"}
        
        res = []
        idx = 0
        if digits:
            self.dfs(digits, idx, "", mapping, res)
        return res
    
    def dfs(self, digits, idx, perm, mapping, res):
        
        if len(perm) == len(digits):
            res.append(perm)
            return
        
        for i in range(len(mapping[digits[idx]])):
            
            self.dfs(digits, idx+1, perm + mapping[digits[idx]][i], mapping,res)


                
                
