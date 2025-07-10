class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        # 5 - 5*4*3*2*1
        # 10
        # 
        count_two = 0
        count_five = 0

        def helper(n):
            nonlocal count_two, count_five

            if n in (0,1):
                return 0

            if n % 5 == 0:
                n_copy = n
                while n_copy % 5 == 0:
                    n_copy //= 5
                    count_five += 1
            
            elif n & 1 == 0:
                n_copy = n
                while n_copy & 1 == 0:
                    count_two += 1
                    n_copy >>= 1
            
            # print(n, count_two, count_five)
            return helper(n-1)
        
        helper(n)

        return min(count_five, count_two)


