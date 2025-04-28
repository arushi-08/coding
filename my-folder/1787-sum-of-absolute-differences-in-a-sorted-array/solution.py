class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        
        # get sum of abs diff
        # 2,3,5

        # sum (abs (curr elem - all others) )
        # sum curr elem * n - sum of other elems

        psum = [0]
        for num in nums:
            psum.append(num + psum[-1])

        n = len(nums)
        tsum = sum(nums)
        result = []
        for i, num in enumerate(nums):
            currsum = 0
            for start, end in [(0, i), (i+1, n-1)]:
                
                currsum += abs(num * (end - start + 1) - (psum[end+1] - psum[start]) )
            
            result.append( currsum )
        
        return result

