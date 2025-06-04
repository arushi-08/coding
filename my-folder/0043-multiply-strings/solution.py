class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        # given 2 non-neg ints num1, num2

        # 2 * 3
        
        if num1 == '0' or num2 == '0': return '0'
        
        ans = [0] * (len(num1)+len(num2))

        for i in range(len(num1)-1,-1,-1):
            for j in range(len(num2)-1,-1,-1):

                carry_idx = i+j
                mul_idx = i+j+1

                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                mul += ans[mul_idx]

                ans[carry_idx] += mul//10
                ans[mul_idx] = mul % 10
                # print(ans, mul)
        
        return ''.join([str(i) for i in ans]).lstrip('0')


