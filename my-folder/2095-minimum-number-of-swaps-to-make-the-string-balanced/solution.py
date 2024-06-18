class Solution:
    def minSwaps(self, s: str) -> int:
        
        stack = []
        slist = list(s)
        closingextra = []
        openingextra = []
        swapst = -1
        count = 0
        for i in range(len(slist)):
            if slist[i] == '[':
                stack.append(slist[i])
            elif stack:
                stack.pop()
            else:
                if swapst != -1:
                    slist[i], slist[swapst] = slist[swapst], slist[i]
                    swapst = -1
                else:
                    swapst = i
                    count += 1
        # if stack:
        if swapst:
            print(swapst)
        return count
            
