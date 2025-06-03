class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

        """

        """

        st = 0
        ed = len(numbers)-1

        while st < ed:
            currsum = numbers[st] + numbers[ed]
            if currsum == target:
                return [st+1, ed+1]
            
            if currsum > target:
                ed -= 1
            else:
                st += 1
        

