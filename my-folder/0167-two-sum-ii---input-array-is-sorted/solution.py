class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

        # 2 pointer

        st = 0
        ed = len(numbers)-1

        while st < ed:
            add = numbers[st] + numbers[ed]
            if add == target:
                return [st+1, ed+1]

            if add < target:
                st += 1
            else:
                ed -= 1

        return  
