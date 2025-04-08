class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        # given array of non-negative integers arr
        # initially positioned at start index
        # jumps = i+arr[i], i-arr[i]
        # reach index val 0


        # graph?
        if arr[start] == 0: return True
        if len(arr) == 1: return False

        queue = deque()
        queue.append(start)
        visited = set()
        while queue:
            curr = queue.popleft()
            if arr[curr] == 0:
                return True

            for next_idx in [curr + arr[curr], curr - arr[curr]]:
                if 0 <= next_idx < len(arr):
                    if next_idx not in visited:
                        queue.append(next_idx)
                        visited.add(next_idx)
        
        return False

            
