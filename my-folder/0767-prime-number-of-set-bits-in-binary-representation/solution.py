class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        
        count = 0
        for num in range(left, right+1):
            count_set = 0
            numcopy = num
            while num:
                if num & 1:
                    count_set += 1
                num >>= 1

            if count_set == 1:
                is_prime = False
            elif count_set in (2,3,5):
                is_prime = True

            else:
                sqrt_count_set = int(count_set**0.5)
                # print(count_set, sqrt_count_set)
                is_prime = True
                
                for i in range(2, sqrt_count_set+1):
                    if count_set % i == 0:
                        is_prime = False
                        break
            if is_prime:
                # print('num prime', numcopy)
                count += 1
        return count
