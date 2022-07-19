from collections import Counter
from heapq import heapify
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_dict = Counter(nums)
        freq_array = [0] * (len(nums) + 1)
        for key, val in freq_dict.items():
            if not freq_array[val]:
                freq_array[val] = []
            freq_array[val].append(key)
        # print(freq_array)
        ans = []
        for i in range(len(freq_array)-1,-1,-1):
            if k == 0:
                break
            if not freq_array[i]:
                continue
            for j in range(len(freq_array[i])):
                # print("here", freq_array[i], j)
                ans.append(freq_array[i][j])
                k -= 1
        
        return ans
                
            
