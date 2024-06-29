class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        
        # 3:1 2:2 1:2 7:1
        # have to incrememt 2 by 2 have to increment 1 by 4
        # 3 2 4 1 5 7
        # 1 1 2 2 3 7
        #   1,1,1
        # 2:3 1:1
        nums.sort()
        
        counter = [0] * (max([len(nums)] + nums)  + 1)
        # print(len(counter), len(nums), max(nums))
        for i in range(len(nums)):
            counter[nums[i]] += 1
        
        emptyspaces = []
        for i in range(nums[0], len(counter)):
            if counter[i] == 0:
                emptyspaces.append(i)
        
        # print('emptyspaces', emptyspaces[-1])
        hmap = {}
        ans = 0
        ptr = 0
        for i in range(len(nums)):
            if ptr == len(emptyspaces):
                emptyspaces.append(emptyspaces[-1]+1)
                # print(ptr, emptyspaces[ptr-1], nums[i])
                # break
            if nums[i] in hmap:
                # print("emptyspaces[ptr]", emptyspaces[ptr])
                # print("nums[i]", nums[i])
                while emptyspaces[ptr] < nums[i]:
                    ptr += 1
                    if ptr == len(emptyspaces):
                        emptyspaces.append(nums[i]+1)

                if nums[i] < emptyspaces[ptr]:
                    ans += emptyspaces[ptr] - nums[i]
                    nums[i] = emptyspaces[ptr]
                    # print("here", ans)
                    ptr += 1
                else:
                    # print("here?", nums[i], emptyspaces[ptr])
                    pass
            if i+1 < len(nums) and ptr < len(emptyspaces) and nums[i+1] > emptyspaces[ptr]:
                ptr += 1
            hmap[nums[i]] = 1
        
        return ans

        # hmap = Counter(nums)
        # ans = 0
        # newhmap = {}
        # # greater_than_current_hmap = {}
        # # for k in hmap:

        # for k in hmap:
        #     while hmap[k] > 1:
        #         newk = k
        #         while newk in hmap or newk in newhmap:
        #             ans += 1
        #             newk += 1 
        #         if newk not in hmap:
        #             newhmap[newk] = 1
        #             hmap[k] -= 1
        
        # return ans

