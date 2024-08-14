class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        
        hmap = Counter(nums)

        ans = 0
        for num in nums:
            if target.startswith(num):
                second_half = target[len(num):]
                if second_half in hmap:
                    ans += hmap[second_half]
                
                if second_half == num:
                    ans -= 1
        
        return ans


            

