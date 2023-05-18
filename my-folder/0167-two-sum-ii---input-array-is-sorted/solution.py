class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range(len(numbers)):
            if numbers[i] in hmap:
                return [hmap[numbers[i]][1]+1, i+1]
            else:
                hmap[target - numbers[i]] = [numbers[i], i]

