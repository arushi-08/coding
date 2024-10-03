class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        # if total sum not divisible return False

        if sum(arr) % k != 0: return False

        # k = 5
        # freq = 2 1 1 1 1
        # idx  = 0 1 2 3 4
        # populate freq list by x modulo k
        # (x + k) % k is done for -ve nos

        freq = [0]*k
        for x in arr:
            freq[((x % k) + k) % k] += 1

        print(freq)

        for i in range(len(freq)):
            if 0 <= k - i < len(freq) and freq[i] != freq[k-i]:
                return False
        
        return True


