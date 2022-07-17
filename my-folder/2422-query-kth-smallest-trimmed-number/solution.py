from heapq import heapify, heappush, heappop
class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        """loop on queries
            trim based on q[-1], 
            to find q[0]th smallest no use maxheap?
            
        """
        if not nums: return []
        
        ans = []
        for i in range(len(queries)): 
            temp_nums = [[int(n[-queries[i][-1]:]), idx] for idx, n in enumerate(nums)] # check this
            heapify(temp_nums)
            for _ in range(queries[i][0]-1):
                heappop(temp_nums)
            _, idx = heappop(temp_nums)
            ans.append(idx)
        
        return ans
            
            
            
        
        
