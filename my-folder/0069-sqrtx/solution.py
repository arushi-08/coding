class Solution:
    def mySqrt(self, x: int) -> int:
        ans = 0
        if x == 1:
            return 1
        left = 1
        right = x
        while(left <= right):
            mid = (right + left) // 2
            # print(mid)
            if mid*mid <= x and (mid+1)*(mid+1)>x:
                return mid
            if mid*mid < x:
                left = mid + 1
            else:
                # print("enter")
                right = mid - 1
        
        return 0
        
#         for i in range(1, x):
#             if i*i <= x:
#                 ans = i
#         return ans
