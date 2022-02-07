class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left , right = 0, len(nums) - 1
        pivot = -1
        if not len(nums):
            return -1
        if len(nums) == 1:
            if nums[0] != target:
                return -1
            else:
                return 0
        
        while(left <= right):
            mid = (left + right) // 2
            if nums[mid] == target:
                # print('ans', mid)
                return mid
            if mid + 1 <= right and nums[mid] > nums[mid+1]:
                pivot = mid
                break
            else:
                # 
                right = mid - 1
                if left > right and pivot == -1:
                    right = len(nums) - 1
                    left = mid + 1
        
        if pivot > -1:
            print(pivot)
            count = 0
            for arr in [nums[:pivot+1], nums[pivot+1:]]:
                if not count:
                    left, right = 0, pivot
                else:
                    left, right = pivot+1, len(nums)-1
                while(left <= right):
                    mid = (left + right) // 2
                    if nums[mid] == target:
                        return mid 
                    if nums[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                count += 1
            return -1
            
        else:
            return -1
