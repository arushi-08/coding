class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        # sum of odd indexed values = even indexed values
        # remove 1 index and make odd index = even index

        # iterate on nums
        # remove current index
        # nums will change indices
        # else from even sum if idx is even
        # count number of indices
        
        # oddsum is always oddsum
        # evensum is always evensum
        count = 0
        sum1 = 0
        sum2 = 0
        prefix_hmap = {}
        for i in range(len(nums)):
            prefix_hmap[i] = [sum1, sum2]
            if i % 2 == 1:
                sum1 += nums[i]
            else:
                sum2 += nums[i]
        # print("prefix_hmap", prefix_hmap)
        sum1 = 0
        sum2 = 0
        postfix_hmap = {}
        for i in range(len(nums)-1,-1,-1):
            postfix_hmap[i] = [sum1, sum2]
            if i % 2 == 1:
                sum1 += nums[i]
            else:
                sum2 += nums[i]
        # print("postfix_hmap", postfix_hmap)
        for i in range(len(nums)):
            s1, s2 = prefix_hmap[i]
            s3, s4 = postfix_hmap[i]
            if s1 + s4 == s2 + s3:
                count += 1
        return count
