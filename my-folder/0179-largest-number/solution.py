class LargerNumKey(str):
    def __lt__(x,y):
        return x+y>y+x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        nums = [str(i) for i in nums]

        nums.sort(key=LargerNumKey)

        ans = ''.join(nums)

        if int(ans) == 0:
            return '0'

        return ans



