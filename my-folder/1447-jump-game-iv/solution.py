class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # bfs
        elem_to_idx = defaultdict(list)
        for i in range(len(arr)-1,-1,-1):
            elem_to_idx[arr[i]].append(i)
        
        queue = deque()
        queue.append((0,0))
        visited = {0}
        last_element = arr[-1]

        while queue:
            curr, n_jumps = queue.popleft()
            if curr == len(arr) - 1:
                return n_jumps
            
            if arr[curr] in elem_to_idx:
                next_range = elem_to_idx[arr[curr]] + [curr-1, curr+1]
                del elem_to_idx[arr[curr]]
            else:
                next_range = [curr-1, curr+1]
            
            for nextidx in next_range:
                if 0 <= nextidx < len(arr):
                    if nextidx not in visited:
                        queue.append((nextidx, n_jumps+1))
                        visited.add(nextidx)
        
        return -1

