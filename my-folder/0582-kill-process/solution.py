class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        

        process_map = defaultdict(list)

        for parent, process in zip(ppid, pid):
            process_map[parent].append(process)
        
        visited = set()
        visited.add(kill)
        self.get_all_children(kill, process_map, visited)
        return list(visited)

    
    def get_all_children(self, root, hmap, visited):

        if not hmap[root]:
            return
        
        for child in hmap[root]:
            if child not in visited:
                visited.add(child)
                self.get_all_children(child, hmap, visited)
        

