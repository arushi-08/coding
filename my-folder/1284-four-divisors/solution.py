class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        
        # find int in nums that have 4 divisors
        # sum the divisors
        visited = {}
        ans = 0
        for num in nums:
            if num in visited:
                count_divs, sum_divs = visited[num]
                
            else:
                sqrt_num = int((num ** 0.5)+ 1)
                count_divs = 0
                sum_divs = 0
                for i in range(1, sqrt_num):
                    if num % i == 0:
                        count_divs += 1
                        sum_divs += i
                        if num // i != i:
                            count_divs += 1
                            sum_divs += num // i
                visited[num] = (count_divs, sum_divs)
            if count_divs == 4:
                ans += sum_divs
        
        return ans
