from collections import Counter
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(res, currans, index):
            if res == 0:
                ans.append(currans.copy())
                return
            if res < 0:
                return
            for i in range(index, len(candidates)):
                currans.append(candidates[i])
                backtrack(res-candidates[i], currans, i)
                currans.pop()
        ans = []
        backtrack(target, [], 0)
        return ans
