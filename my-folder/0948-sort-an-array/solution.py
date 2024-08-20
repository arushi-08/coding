class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        self.merge_sort(nums, 0, len(nums)-1)
        return nums
    
    def merge_sort(self, nums, st, ed):
        
        if st == ed:
            return

        mid = (st+ed)//2
        self.merge_sort(nums, st, mid)
        self.merge_sort(nums, mid+1, ed)

        self.merge(nums, st, mid, ed)
    
    def merge(self, nums, st, mid, ed):

        nums1 = nums[st:mid+1]
        nums2 = nums[mid+1:ed+1]
        
        i = 0
        j = 0
        k = 0
        temp = [0]*len(nums1+nums2)

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                temp[k] = nums1[i]
                i += 1
            else:
                temp[k] = nums2[j]
                j += 1
            k += 1
        
        while i < len(nums1):
            temp[k] = nums1[i]
            i += 1
            k += 1
        
        while j < len(nums2):
            temp[k] = nums2[j]
            j += 1
            k += 1
        
        nums[st:ed+1] = temp


        

