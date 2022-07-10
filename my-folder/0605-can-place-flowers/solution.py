class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        i = 0
        while i < len(flowerbed):
            if n == 0: return True

            can_plot = True
            if i - 1 >= 0 and flowerbed[i-1]:
                can_plot = False
            if i + 1 < len(flowerbed) and flowerbed[i + 1]:
                can_plot = False
                i += 3
            
            if i < len(flowerbed) and flowerbed[i]:
                can_plot = False
                i += 2
                
            if can_plot:
                flowerbed[i] = 1
                n -= 1
                i += 2
        
        if n == 0: return True
        return False
                
