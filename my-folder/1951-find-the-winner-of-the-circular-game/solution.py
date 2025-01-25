class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        # find winner i.e., 1 person that's left
        # sitting in circle
        # numbered 1 to n - clockwise order
        # i to i+1
        # count next k friends including curr friend
        # the last friend you counted leaves the circle 
        # loses the game

        i = 0
        friends = [1] * n
        flen = n
        last_idx = 0

        while n > 1:
            f_count = 0
            for j in range(i, i+flen*k):
                j = j % flen
                if friends[j]:
                    f_count += 1
                if f_count == k:
                    friends[j] = 0
                    last_idx = j
                    break
            
            i = last_idx
            n -= 1

        for i, fred in enumerate(friends):
            if fred:
                return i+1

