class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        # def dfs(n):
        #     if n == 0:
        #         return 0
            
        #     count = 0
        #     for i in [3, 2]:
        #         n -= i
        #         count +=  1
        #         print("n", n, "q", q,"count",count)
        #         count += dfs(q)

        #     return count

        hmap = Counter(nums)
        count = 0
        for k in hmap:
            if hmap[k] == 1:
                return -1
            if hmap[k] % 3 == 0:
                count += hmap[k] // 3
            else:
                n = hmap[k]
                while n:
                    n -= 2
                    count += 1
                    if n % 3 == 0:
                        count += n // 3
                        break
        
        return count

