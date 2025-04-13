class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        st = 0
        ed = len(nums)-1

        while st <= ed:
            mid = (st + ed) // 2

            if target in (nums[st], nums[mid], nums[ed]):
                return True
            # print('mid', mid, 'st', st, 'ed', ed)

            if nums[st] == nums[mid] and nums[mid] == nums[ed]:
                st += 1
                ed -= 1
                continue
            # 1,1,1,2,1,1,1,1,1
            if nums[st] <= nums[mid]:
                if nums[st] <= target < nums[mid]:
                    ed = mid - 1
                else:
                    st = mid + 1
            else:
                if nums[mid] < target <= nums[ed]:
                    st = mid + 1
                else:
                    ed = mid - 1
        
        return False

            

