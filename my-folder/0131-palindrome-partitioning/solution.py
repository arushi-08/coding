class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        curr = []
        self.helper(s, curr, res)
        return res
    
    def ispalindrome(self, s):
        i = 0
        j = len(s) - 1
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
        
    def helper(self, s, curr, res):
        if not s:
            res.append(curr.copy())
            return
        
        for i in range(1, len(s)+1):
            # print(s[:i], i)
            if self.ispalindrome(s[:i]):
                curr.append(s[:i])
                # print("inside", curr)
                self.helper(s[i:], curr, res)
                curr.pop()
            else:
                continue
        
