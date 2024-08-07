class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        

        # aim - 1 to target should be obtainable
        # return min # of coins to add to coins list to get to aim


        # main part- find all subsequence sums of coins
        # binary search
        # coins.sort()
        # coins_psum = [coins[0]]
        # for i in range(1, len(coins)):
        #     coins_psum.append(coins_psum[-1]+coins[i])

        # coins_psum_set = set(coins_psum + coins)

        # def is_obtainable(mid, coins_psum_set):
        #     nonlocal target

        #     for i in range(1, target):
        #         if i not in coins_psum_set:
        #             if mid:
        #                 mid -= 1
        #             else:
        #                 return False
            
        #     return True


        # start = 1
        # end = target - len(coins)
        # count = 0
        # while start <= end:
        #     mid = (start + end) // 2
        #     if is_obtainable(mid, coins_psum_set):
        #         start = mid
        #     else:
        #         end = mid + 1

        # return start


# main part
# what should binary search be on?
# should be on the things that we want
# min # of coins - FFFTTTT
# 1 to target - number of coins we have - search space for coins to be added

# for each mid # of coins added, we should obtain 1 to target nos - how to do this?
# 

# begin by attempting to bridge gap between 1st 2 values if this is > 1 
# if its possible to obtain all coins that lie between 1st 2 coins
#       store the sum of those coins
# if not
#       create a suitable coin and add it to sum

        coins.sort()
        ssum = 0
        count = 0 

        for i in range(len(coins)):
            while ssum < coins[i]-1:
                ssum = 2 * ssum + 1
                count += 1
            ssum += coins[i]
        
        while ssum < target:
            count += 1
            ssum = 2*ssum + 1

        return count
