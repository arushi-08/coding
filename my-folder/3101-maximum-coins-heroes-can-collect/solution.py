class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        
        # go over each hero
        #  see how many monsters it can kill
        monsters_coins = [(m, c) for m, c in zip(monsters, coins)]
        monsters_coins.sort()

        monsters_coins_psum = [monsters_coins[0][1]]
        for i in range(1, len(monsters_coins)):
            monsters_coins_psum.append(monsters_coins_psum[-1] + monsters_coins[i][1])
        
        ans = [0] * len(heroes)

        for i in range(len(heroes)):
            start = 0
            end = len(monsters_coins) - 1
            monster_upper_limit = -1
            while start <= end:
                mid = (start + end) // 2
                if monsters_coins[mid][0] <= heroes[i]:
                    monster_upper_limit = mid
                    start = mid + 1
                else:
                    end = mid - 1
            
            if monster_upper_limit != -1:
                ans[i] = monsters_coins_psum[monster_upper_limit]

        return ans
