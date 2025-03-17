class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        # divide array into equal pairs

        # each elem belongs to 1 pair
        # elems present in a pair are equal

        # each num in a pair

        num_hmap = Counter(nums)

        for k, v in num_hmap.items():
            if v & 1 == 1:
                return False
        
        return True
