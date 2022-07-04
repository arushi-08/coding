class Solution:
    def trap(self, height: List[int]) -> int:
        
        i = 0
        max_val = 0 
        storage_left = {}
        while i < len(height):
            if height[i] > max_val:
                max_val = height[i]
            else:
                storage_left[i] = max_val - height[i]
            i += 1
        
        i = len(height)-1
        max_val = 0 
        storage_right = {}
        while i > -1:
            if height[i] > max_val:
                max_val = height[i]
            else:
                storage_right[i] = max_val - height[i]
            i -= 1
        
        ans = 0
        for i in storage_left:
            if i in storage_right:
                ans += min(storage_left[i], storage_right[i])
        return ans
            
