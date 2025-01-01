class Solution:
    def minimizeSet(self, div1: int, div2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        def get_lcm(div1, div2):
            gcd = math.gcd(div1, div2)
            return div1*div2//gcd
        st = 2
        ed = 10**10
        lcm = get_lcm(div1, div2)
        ans = 0
        while st <= ed:
            mid = (st + ed)//2
            a = mid - (mid//div1)
            b = mid - (mid//div2)
            # c is nums that are not div by div1 or div2
            c = mid - (mid//div1) - (mid//div2) + (mid//lcm)
            # print('a', a, 'b', b, 'c', c)
            if a>=uniqueCnt1 and b>=uniqueCnt2 and a+b-c>=(uniqueCnt1+uniqueCnt2):
                ans = mid
                ed = mid - 1
            else:
                st = mid + 1
        
        return ans
