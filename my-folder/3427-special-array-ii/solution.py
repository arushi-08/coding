class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        # psum is useful here because 
        # if all adjacent nos are diff parity then count keeps incrementing
        # like normal index
        # otherwise psum count doesn't increment and so
        # we can detect if start-end range is special or not

        arr = [0] * (len(nums) - 1)
        for i in range(len(nums)-1):
            if nums[i] % 2 != nums[i+1] % 2:
                arr[i] = 1
            else:
                arr[i] = 0
        
        psum = [0]
        cursum = 0
        for i in arr:
            cursum += i
            psum.append(cursum)
        
        ans = []
        for s,e in queries:
            if psum[e] - psum[s] == e-s:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans
