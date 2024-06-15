from functools import cmp_to_key
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        # maximize profit after doing k distinct tasks

        # use ordereddict to convert capital: profit
        capprofitlist = []
        for i in range(len(capital)):
            capprofitlist.append((capital[i], profits[i]))
        
        capprofitlist.sort(key = lambda x: x[0])
# of all the projects that have capital <= w, you have to pick the one which has the highest profit
        totprofits = w
        # print(capprofitlist)
        maxheap = []
        i = 0
        if capprofitlist[0][0] > w:
            return 0

        while True:
            while i < len(capprofitlist) and capprofitlist[i][0] <= w:
                heappush(maxheap, -capprofitlist[i][1])            
                i += 1
            
            if k and maxheap:
                element = -heappop(maxheap)
                w += element
                totprofits += element
                k -= 1
            else:
                break
        return totprofits
        

