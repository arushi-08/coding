class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        # ord('A') * 26 ** #position
        # 28 = 1 * 26 ** 1  + 2 * 26 ** 0
        # 701 = 26 * 26 ** 1 + 25 * 26 ** 0

        # 142 = 1 * 10 ** 2 + 4 * 10 ** 1 + 2 * 10 ** 0
        i = 8
        word = ''
        
        while columnNumber:
           columnNumber -= 1
           word += chr(columnNumber % 26 + ord('A'))
           columnNumber //= 26
        
        return word[::-1]

