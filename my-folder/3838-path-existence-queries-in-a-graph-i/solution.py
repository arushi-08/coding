class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        
        result = []
        # binary search
        path = set(nums)
        
        # only breaks happen when adj element diff > maxDiff

        path_list = [0] * n
        next_batch = 0
        for i in range(len(nums)-1):
            path_list[i] = next_batch
            if nums[i+1] - nums[i] > maxDiff:
                next_batch += 1
        path_list[-1] = next_batch
        
        for q in queries:
            u, v = q
            result.append( path_list[u] == path_list[v] )

        return result
