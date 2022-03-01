class Solution:
            
    def search_array(self, nums, target):
        
        left = 0
        right = len(nums) - 1
        print(nums[0])
        if nums[0] == target:
            return 0
        
        while(left <= right):
            
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
    
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1
        pivot = -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            return -1
        
        while(left <= right):
            mid = (left + right) // 2
            # print(mid, nums[mid] , nums[mid+1] )
            if mid + 1 < len(nums) and nums[mid] > nums[mid+1]:
                pivot = mid
                break
            else:
                left = mid + 1
                if left > right and pivot == -1:
                    left = 0
                    right = mid - 1
        print("pivot", pivot)
        if pivot > -1:
            nums2 = nums[:pivot+1]
            nums1 = nums[pivot+1:]
            if nums2[0] > target:
                ans = self.search_array(nums1, target)
                if ans >= 0:
                    return ans + pivot + 1
                return ans
            else:
                ans = self.search_array(nums2, target)
                return ans
        
        else:
            return  self.search_array(nums, target)
