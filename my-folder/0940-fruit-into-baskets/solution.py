class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        fmap = {}
        maxcount = 0
        currcount = 0

        queue = deque()

        for i in range(len(fruits)):

            if fruits[i] not in queue:
                if len(queue)==2:
                    fruitpop = queue.popleft() 

                    if fruits[i-1] == fruitpop:
                        currcount = i - fmap[queue[0]] - 1 
                        queue.pop()
                        queue.append(fruitpop)

                    elif fruits[i-1] == queue[0]:
                        currcount = i - fmap[fruitpop] - 1

                queue.append(fruits[i])

            fmap[fruits[i]] = i
            currcount += 1
            maxcount = max(currcount, maxcount)

        return maxcount


# 1,2,1
# 1:2
# 2:1

# 0,1,2,2,0,0,0
# 0:1
# 1:1
# 2:2


