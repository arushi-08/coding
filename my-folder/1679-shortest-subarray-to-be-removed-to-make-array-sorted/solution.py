class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        
        # remove shortest subarray after which remaining elements are non-decreasing
        # [1,2,3,10,4,2,3,5]
        # [1,2,3,3,5] remove [10,4,2]

        # remove shortest
        # keep seeing if current element makes the arr non-decreasing
        # stack is empty -> append
        # [1], current 2
        # stack[-1] < 2 -> append
        # [1,2], current 3
        # stack[-1] < 3 -> append
        # [1,2,3], current 10 -> append
        # [1,2,3,10], current 4
        # stack[-1] > 4 -2 options-> 4 can be ignored or 10 can be popped from stack
        # if we ignore 4 then it's counted in removing subarray
        # if next element 
        # 


        # convert question to get max subarray possible to make array sorted
        # [1,2,3,10] > 4
        #  since 4 is smaller
        #   keep 4
        # try to make it like LIS question

        # 2 options, keep previous lis or start new 

        # dp = [()] * len(arr)
        # dp[0] = (arr[0], 1)
        
        # for i in range(1, len(arr)):
        #     if arr[i] >= dp[i-1][0]:
        #         dp[i] = (arr[i],dp[i-1][1] + 1)
        #     else:
        #         j = i-1
        #         while j >= 0 and arr[j] > arr[i]:
        #             j -= 1
        #         if j < 0:
        #             dp[i] = dp[i-1]
        #         else:
        #             if dp[i-1][1] > dp[j][1] + 1:
        #                 dp[i] = (dp[j][0], dp[j][1]+1)
        #             else:
        #                 dp[i] = dp[i-1]
        
        # print(dp)
        # return len(arr) - dp[-1][1]


        # this has to be sorted: arr[:start] + arr[end+1:]

        # find longest prefix from left of array
        # left - last index of this prefix
        # if left reaches end of array then array is already sorted

        left = 0
        while left < len(arr)-1 and arr[left] <= arr[left + 1]:
            left += 1
        
        if left == len(arr):
            return 0
        # from right of array, find longest suffix
        # right - first index of this prefix

        right = len(arr)-1
        while right > 0 and arr[right] >= arr[right - 1]:
            right -= 1

        # calculate length of subarray that would need to be removed if we keep only longest prefix and suffix
        # i.e., removing entire middle section

        subarry_len = min(len(arr)-1-left, right)
        
        i = 0
        j = right

        while i < j:
            while i + 1 < j and j < len(arr) and arr[i] <= arr[j] and arr[j - 1] <= arr[j]:
                j -= 1

            while j < len(arr) and arr[i] > arr[j]:
                j += 1

            subarry_len = min(subarry_len, j - i - 1)

            if arr[i] > arr[i+1]:
                break
            
            i += 1

        return subarry_len
        # merge prefix and suffix using 2 pointers
        # i at beginining of prefix
        # j at begining of suffix
        # can elements from prefix connect with elements from suffix?
        # in sorted order

        # each time arr[i] <= arr[j] is satisfied, update result with length of subarr removed
        # if we retain elements from i to j

        # return result

