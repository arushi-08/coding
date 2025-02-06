class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        
        # given array of distinct positive int
        # return num of tuples (a,b,c,d) : a*b = c*d
        # a!=b!=c!=d
        # [2,3,4,6]
        # find 2 nums whose product = product of 2 other nums
        # 

        # do nested loop - search every (i,j) pair
        # store their product in hashmap
        # 8 possible tuples for each distinct pair of pairs
        hmap = defaultdict(list)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                hmap[nums[i]*nums[j]].append([i,j])
        
        ans = 0
        for k, v in hmap.items():
            if len(v) > 1:
                ans += 8*len(v)*(len(v)-1)//2
        
        return ans

# 2 - 1*8
# 3 - 3*8
# 4 - 6*8
# 5 - 10
# relation
# 
# 1 link, 3*1 links, 3*2 links
# 2,        3,          4 
#  
# 
# if there are 4 nodes, how many total number of edges can there be?
# 2/2
# 3 nodes -> 3*2/2
# 4 nodes -> 4*3/2
# 
