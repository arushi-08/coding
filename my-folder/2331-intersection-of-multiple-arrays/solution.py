class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        
        # 2d arr
        # check for common elems in all num

        # [[1,2,3,4,5],
        #  [1,2,3,4],
        #  [3,4,5,6]]

        hmap = defaultdict(int)
        ans = []
        n_arr = len(nums)
        for num in nums:
            for elem in num:
                hmap[elem] += 1
                if hmap[elem] == n_arr:
                    ans.append(elem)
        return sorted(ans)
        
            



