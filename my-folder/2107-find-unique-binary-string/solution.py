class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        visited = set(nums)

        def dfs(bin_string, res, visited):
            if len(bin_string) == len(nums):
                if bin_string in visited:
                    return False
                res.append(bin_string)
                return True
            
            for i in ['0', '1']:
                if dfs(bin_string+i, res, visited):
                    return True
            return False
        
        res = []
        dfs('', res, visited)
        return res[0]


