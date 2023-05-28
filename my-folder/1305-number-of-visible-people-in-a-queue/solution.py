class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(heights)
        stack.append(0)
        for i in range(1, len(heights)):
            while stack and heights[i] > heights[stack[-1]]:
                top = stack.pop()
                ans[top] += 1
            if stack:
                ans[stack[-1]] += 1
            stack.append(i)
        
        return ans

        
