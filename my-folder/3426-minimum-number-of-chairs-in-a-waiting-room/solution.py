class Solution:
    def minimumChairs(self, s: str) -> int:
        
        # min num of chairs needed
        n_chairs = 0
        min_chairs = 0
        for char in s:
            if char == 'E':
                n_chairs += 1
            else:
                n_chairs -= 1
            min_chairs = max(min_chairs, n_chairs)
        
        return min_chairs

