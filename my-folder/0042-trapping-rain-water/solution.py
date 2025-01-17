class Solution:
    def trap(self, height: List[int]) -> int:
        # 2 pointers:
        # shift the minimum towards the arr
        # ans += max_ptr - height[ptr]
        left = 0
        right = len(height)-1
        left_max = 0
        right_max = 0
        ans = 0
        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                ans += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                ans += right_max - height[right]
                right -= 1
        
        return ans

