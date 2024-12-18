class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        potions.sort()
        ans = []
        for spell in spells:
            st = 0
            ed = len(potions)
            begin = ed
            while st <= ed:
                mid = (st + ed)//2
                if mid < len(potions) and potions[mid] * spell >= success:
                    begin = mid
                    ed = mid - 1
                else:
                    st = mid + 1
            
            ans.append(len(potions) - begin)
        
        return ans
            
            
