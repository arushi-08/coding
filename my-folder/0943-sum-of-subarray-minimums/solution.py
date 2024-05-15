class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        stack = []
        ans = 0

        for i in range(len(arr) + 1):

            while stack and (i == len(arr) or arr[i] <= arr[stack[-1]]):
                popped = stack.pop()
                if not stack:
                    left_boundary = -1
                else:
                    left_boundary = stack[-1]
                right_boundary = i
                ans += arr[popped] * (popped-left_boundary) * (right_boundary-popped)

            stack.append(i)

        return ans % (10 ** 9 + 7)
