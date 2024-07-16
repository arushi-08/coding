class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        
        if num == 1: return False
        sqrtnum = int(num**0.5)
        
        cursum = 1
        for i in range(2, sqrtnum+1):
            if not num%i:
                cursum += i + num//i

        return cursum == num
            

