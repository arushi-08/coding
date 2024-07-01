class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        oddcount = 0
        ans = 0
        st = 0
        st_ones = 0
        ed_ones = 0
        ones_list = []

        for i in range(len(nums)):

            if nums[i] & 1 == 1:
                if not oddcount:
                    st_ones = i
                oddcount += 1
                ones_list.append(i)

                if oddcount == k:
                    ed_ones = i

            if oddcount == k and (
                (i+1 < len(nums) and nums[i+1] & 1 == 1) or i+1 == len(nums)
                ):
                ans += (st_ones-st+1) * (i-ed_ones+1)
                oddcount -= 1
                st = 0 

                if len(ones_list) >= 2:
                    if ones_list[1] - ones_list[0] > 1:
                        st = ones_list[0] + 1

                    st_ones = ones_list[1]
                else:
                    st_ones = i + 1
                
                if not st:
                    st = min(st_ones, ones_list[-1]+ 1) 

                ones_list.pop(0)

        return ans

                # [0,0,0,1,0,0,1,0,0,0]
                #  0,1,2,3
    
    # [91473,45388,24720,35841,29648,77363,86290,58032,53752,87188,34428,85343,19801,73201]
#       [1,0,0,1,0,1,0,0,0,0,0,1,1,1]


# [45627,50891,94884,11286,35337,46414,62029,20247,72789,89158,54203,79628,25920,16832,47469,80909]
#  [1,1,0,0,1,0,1,1,1,0,1,0,0,0,1,1]


    # 0 - 0 + 1 * 4 - 3 = 1
    # oddcount = 1
    # st = 4
    # st_ones = 4
