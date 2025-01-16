class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        self.merge_sort(nums, 0, len(nums)-1)
        return nums
    
    def merge_sort(self, nums, st, ed):
        if st >= ed : return

        mid = (st+ed)//2

        self.merge_sort(nums, st, mid)
        self.merge_sort(nums, mid+1, ed)
        self.merge(nums, st, ed, mid)
    
    def merge(self, nums, st, ed, mid):
        temp = []
        i = st
        j = mid+1
        while i <= mid and j <= ed:
            if nums[i] < nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1
        while i <= mid:
            temp.append(nums[i])
            i += 1
        while j <= ed:
            temp.append(nums[j])
            j += 1
        
        for i in range(st, ed+1):
            nums[i] = temp[i-st]

