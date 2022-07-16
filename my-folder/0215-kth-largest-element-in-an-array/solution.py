from heapq import heappush, heappushpop
import random
class Solution:
    def findKthLargest(self, nums, k):
        # convert the kth largest to smallest
        if nums:
            return self.findKthSmallest(nums, len(nums)+1-k)
        return -1
    
    def findKthSmallest(self, nums, k_smallest):
        pivot = random.randint(0, len(nums)-1)
        pivot = self.partition(nums, 0, len(nums)-1, pivot)
        if k_smallest > pivot + 1:
            return self.findKthSmallest(nums[pivot+1:], k_smallest-pivot-1)
        elif k_smallest < pivot + 1:
            return self.findKthSmallest(nums[:pivot], k_smallest)
        else:
            return nums[pivot]
    
    def partition(self, nums, left, right, pivot):
        
        temp_left = left
        for i in range(left, right):
            if nums[i] <= nums[right]:
                nums[i], nums[temp_left] = nums[temp_left], nums[i]
                temp_left += 1
        nums[temp_left], nums[right] = nums[right], nums[temp_left]
        
        return temp_left
        
            
        


