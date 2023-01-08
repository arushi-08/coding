from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        # define maj_cand1, maj_cand2, counter1, counter2
        maj_cand1, maj_cand2, counter1, counter2 = None, None, 0, 0

        for n in nums:
            if maj_cand1 == n:
                counter1 += 1
            elif maj_cand2 == n:
                counter2 += 1
            elif counter1 == 0:
                maj_cand1 = n
                counter1 += 1
            elif counter2 == 0:
                maj_cand2 = n
                counter2 += 1
            else:
                counter1 -= 1
                counter2 -= 1
            
        ans = []
        for i in [maj_cand1, maj_cand2]:
            if nums.count(i) > len(nums)/ 3:
                ans.append(i)
        
        return list(set(ans))


