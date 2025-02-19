class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        

        # happy string: [a,b,c]
        # s[i] != s[i+1]
        # for all vals
        # e.g. abc, ac, b
        # abcbabcbcb
        # return kth string of sorted lexicographically ordered happy strings

        # get all possible happy strings

        
        def dfs(happy_str, result):
            if len(happy_str) == n:
                result.add(happy_str)
                return
            
            for j in ['a','b','c']:
                if happy_str and happy_str[-1] != j:
                    dfs(happy_str+j, result)


        result = set()
        used = set()
        for i in ['a','b','c']:
            dfs(i, result)
        # print(result)

        if k > len(result): 
            return ""
        return sorted(list(result))[k-1]
