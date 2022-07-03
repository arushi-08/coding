class Solution:
    def get_prefix_sum(self, a):
        dict1 = {0:1}
        sum1 = 0
        for idx, i in enumerate(a):
            if sum(a[:idx+1]) not in dict1:
                dict1[sum(a[:idx+1])] = 1
            else:
                dict1[sum(a[:idx+1])] += 1
        return dict1
        
    def subarraySum(self, a: List[int], k: int) -> int:
        """
        logic: dict = {prefix sum: index}
        target - prefix sum in dict1 count += 1
        """
        # dict1 = self.get_prefix_sum(a)
        dict1 = {0:1}
        count = 0
        sum1 = 0
        for idx, element in enumerate(a):
            sum1 += element
            if sum1 - k in dict1:
                count += dict1[sum1 - k]
            if sum1 not in dict1:
                dict1[sum1] = 1
            else:
                dict1[sum1] += 1
        
        return count
