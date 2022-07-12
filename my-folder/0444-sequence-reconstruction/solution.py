from typing import List
from collections import deque, defaultdict
class Solution:

    def count_parents(self, seqs):
        graph = defaultdict(list)
        map_dict = {}
        for i in range(len(seqs)):
            for j in range(len(seqs[i])-1):
                map_dict[seqs[i][j+1]] = map_dict.get(seqs[i][j+1], 0) + 1
                graph[seqs[i][j]].append(seqs[i][j+1])
        return map_dict, graph
    
    def sequenceReconstruction(self, original: List[int], seqs: List[List[int]]) -> bool:
        map_dict, graph = self.count_parents(seqs)
        queue = deque()
        
        for i in range(len(seqs)):
            for j in range(len(seqs[i])):
                if (seqs[i][j] not in map_dict 
                    and seqs[i][j] not in queue): queue.append(seqs[i][j])
    #     print(queue)
        idx = 0
        top_sort = []
        while len(queue):
            if len(queue) >1 : return False
            if original[len(top_sort)] != queue[0] : return False
            curr = queue.popleft()
            
    #         if original[idx] != curr: return False #check this
            idx += 1
            top_sort.append(curr)
            for child in graph[curr]:
                map_dict[child] -= 1
                if map_dict[child] == 0:
                    queue.append(child)
            
#             for i in range(len(seqs)):
#                 for j in range(len(seqs[i])-1):
#                     if seqs[i][j] == curr:
#     #                     print("enter", seqs[i][j+1])
#                         map_dict[seqs[i][j+1]] -= 1

#                         if seqs[i][j+1] in map_dict and map_dict[seqs[i][j+1]] == 0:
#                             queue.append(seqs[i][j+1])
    #     print("top_sort", top_sort)
        if top_sort == original: return True

        return False
