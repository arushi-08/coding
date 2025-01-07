class Solution:
    def fractionAddition(self, expression: str) -> str:
        # list(map(int)) converts string exp list to int with - and + signs
        # "-1/2+1/42" -> [-1, 2, 1, 42]
        # numerator = numerator * den + denominator * num
        # denominator *= den
        # in final result, return numerator // common_div / denominator // common_div
        
        nums = list(map(int, re.findall(r'[+-]?\d+', expression)))

        numerator = 0
        denominator = 1

        for i in range(0, len(nums), 2):
            num, den = nums[i], nums[i+1]
            numerator = numerator * den + denominator * num
            denominator *= den
        
        common_div = gcd(numerator, denominator)
        return f"{numerator//common_div}/{denominator//common_div}"
