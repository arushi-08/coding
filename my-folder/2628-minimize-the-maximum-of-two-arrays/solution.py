class Solution:
    def minimizeSet(self, div1: int, div2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        
        # arr1 contains uniqueCnt1 elems, each not divisible by div1
        # return min possible max int of either array

        # arr1 = 1, arr2 = 2,3,4 -> return 4

        # get nums that are divisible by div1
        # e.g. div1 = 7, uniqueCnt1 = 10
        # 7*1 = 7 -> add 1 to 10 in place of 7, -> 11, min num is 11
        # 1,2,3,4,5,6,8,9,10,11
        # 15,16,17,18,19,20,22,23,24,25
        # div2 = 4, uniqueCnt2 = 10
        # 13,14,15,17,18,19,21,22,23,25
        # 1,2,3,5,6,9,10,11,13,14
        # 11 + 10 = 21
        # 4*3, 4*4, 4*5 -> 12, 16, 20 -> add 3 to 21 -> 24

        # FFFFTTTTT
        # mid = max of 2 arrays
        # if mid % by any of 2 return false
        # if mid gcd

        # 10 - 10//3 = 7 -> 1,2
        # 10 - 10//5 = 8 -> 1
        # 10 - 10//15 = 10

        # a = mid - mid // div1
        # b = mid - mid // div2
        # c = mid - mid // lcm(div1, div2)
        def get_lcm(div1, div2):
            gcd = math.gcd(div1, div2)
            return div1*div2/gcd

        def is_possible(mid, div1, div2, lcm, uniqueCnt1, uniqueCnt2):
            # div1 divisible can be in arr2
            # div2 divisible can be in arr1
            # nums that are neither divisible can be in either arr1, arr2
            a = mid - mid//div1 # a is nums that can be in div1
            b = mid - mid//div2 # b is nums that can be in div2
            # doubt: c is nums that are not divisible by div1, div2
            c = mid - mid//div1 - mid//div2 + mid//lcm 
            return a >= uniqueCnt1 and b >= uniqueCnt2 and a+b-c >= uniqueCnt1 + uniqueCnt2

        st = 1
        ed = 10**10
        lcm = get_lcm(div1, div2)
        ans = 0
        while st <= ed:
            mid = (st + ed)//2
            if is_possible(mid, div1, div2, lcm, uniqueCnt1, uniqueCnt2):
                ans = mid
                ed = mid - 1
            else:
                st = mid + 1
            
        return ans



