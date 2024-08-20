class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        

        # output: length of set
        # build set for each element in nums
        # note: logic of building set

        # [5,4,0,3,1,6,2]

        # n = 1 -> ans = 1
        # n = 2 -> ans = 2 or 1
        # n = 3 -> [2,0,1] -> ans = 3
        # n = 4 -> [3,2,0,1] -> ans = 4
        #          [2,0,3,1] -> ans = 4
        #          [0,2,3,1] -> ans = 3

        # if element not present on its index -> will contribute to the set
        # if element on its index, set breaks
        # it will not be reachable by other sets

        n_elem_on_its_idx = 0
        
        visited = set()
        current_max_length = 0

        for i in range(len(nums)):
            current_set = set()
            if nums[i] == i:
                n_elem_on_its_idx += 1
                continue
            
            if nums[i] in visited:
                continue

            element = nums[i]
            while element not in current_set:
                current_set.add(element)
                visited.add(element)
                element = nums[element]
            
            current_max_length = max(current_max_length, len(current_set))
            
        if len(nums) == n_elem_on_its_idx:
            return 1
        
        return current_max_length
        # cycle

        # find the longest cycle


        # iterate on the list of nums
            # build set starting at nums[i]
                # store the max (len(set))

        
            # build set starting at nums[i]
            # while loop till duplicate found
                # keep building the set
        
            
        # this is o(n^2) solution

        # [1,2,3,4,5]
        # sort the list
        # then we just move ahead
        # and the max set will be the one in beginining


        # whenever i redirect my path
        # don't dive into coding




