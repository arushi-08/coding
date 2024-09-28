class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        
        maximumHeight.sort(reverse=True)
        hset = set()
        answer = 0
        for m in maximumHeight:
            if m in hset:
                m = self.binary_search(m, hset)
            if m <= 0:
                return -1
            hset.add(m)
            answer += m
        
        return answer

    def binary_search(self, target, hset):

        start = 0
        end = target-1
        result = 0
        while start <= end:
            mid = (start + end)//2
            if mid not in hset:
                result = max(result, mid)
                start = mid + 1
            else:
                end = mid - 1
        
        return result

