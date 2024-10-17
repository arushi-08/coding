class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        heap = []
        for count, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if count != 0:
                heapq.heappush(heap, (count, char))
        result = []
        while heap:
            count, char = heappop(heap)

            if len(result) >= 2 and result[-1] == result[-2] == char:
                if not heap:
                    break
                count2, char2 = heappop(heap)
                result.append(char2)
                count2 += 1
                if count2 != 0:
                    heappush(heap, (count2, char2))
            else:
                result.append(char)
                count += 1

            if count != 0:
                heappush(heap, (count, char))
        
        return ''.join(result)
                
            
