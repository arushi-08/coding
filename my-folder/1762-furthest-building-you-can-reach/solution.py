class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        # priority? ladder or brick
        # if current gap is greater than brick ht -> use ladder
        # else use brick

        
        largest_jump = []
        sumjumps = 0
        i = 1
        while i < len(heights):
            # iterate on the buildings
            # maintaining largest r jumps
            # sum of remaining ones so far
            # break when sum exceeds b

            if heights[i] > heights[i-1]:
                jump = heights[i] - heights[i-1]

                if len(largest_jump) < ladders:
                    heappush(largest_jump, jump)

                elif largest_jump and len(largest_jump) >= ladders:
                    if jump >= largest_jump[0]:
                        sumjumps += heappop(largest_jump)
                        heappush(largest_jump, jump)
                    else:
                        sumjumps += jump
                else:
                    sumjumps += jump
                
                if sumjumps > bricks:
                    return i - 1
            i += 1

        return i - 1
