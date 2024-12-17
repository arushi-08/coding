class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:

        total_shift = 0
        for i in range(len(shift)):
            direction, amount = shift[i]
            if direction == 0:
                total_shift -= amount
            else:
                total_shift += amount
        
        temp = 0
        s_list = [''] * len(s)
        for i in range(len(s)):
            s_list[(i+total_shift) % len(s)] = s[i]

        return ''.join(s_list)
