class Solution:
    def maxArea(self, height: List[int]) -> int:
        # strt ptr, end ptr
        # calculate area = min(start, end) * (end - start)
        # increment the smaller of the start and end ptr elements

        start = 0
        end = len(height)-1
        maxarea = 0
        while start < end:
            maxarea = max(
                maxarea, 
                min(height[start], height[end]) * (end - start)
                )
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return maxarea

