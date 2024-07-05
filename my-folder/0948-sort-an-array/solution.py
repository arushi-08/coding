class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        numscopy = nums.copy()
        numscopy.sort()
        if nums == numscopy: return nums
        else: return numscopy
        self.quicksort(nums, 0, len(nums)-1)
        return nums
    
    def quicksort(self, nums, start, end):
        if start < end:
            pivot = self.pivot(nums, start, end) # pivot = 3 [1,2,3,5]
            self.quicksort(nums, start, pivot-1) # st=0,ed=2
            self.quicksort(nums, pivot+1, end)

    def pivot(self, nums, start, end):
        # 3 pointer approach
        # put all elements less than pivot on left side
        # all element more than pivot on right side

        i = start-1 # position where next <= element will be placed
        pivot = random.randint(start, end)
        nums[pivot], nums[end] = nums[end], nums[pivot]
        for j in range(start, end):
            if nums[j] <= nums[end]:
                i+=1
                nums[i], nums[j] = nums[j], nums[i]
        
        nums[i+1], nums[end] = nums[end], nums[i+1]
        return i + 1
        

