class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        
        # what are the numbers that can be rotated
        """
        6:9
        8
        0
        """
        strobo = {"6":"9", "0":"0", "8":"8", "9":"6", "1":"1"}
        ptr = len(num)-1
        for i in range(len(num)):
            if ptr < i:
                break
            if num[i] not in strobo:
                return False
            if num[i] in strobo:
                if num[ptr] != strobo[num[i]]:
                    return False
                ptr -= 1
        
        return True
