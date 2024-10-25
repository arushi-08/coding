class Solution:
    def removeSubfolders(self, folders: List[str]) -> List[str]:
        
        # if there is a folder that is also a subfolder, remove folder
        # keep base folders
        # /a, /c/d, /c/f

        # build a trie from set
        # iterate on folder
        # if folder[i][0] exists in set
        # /a/b in {'a'}
        #   -> so skip /a/b
        # /c/d not in {'a'}
        #   -> add it
        #   {'a','c'}
        # /c/d/e in {'a', 'c/d'}
            # -> skip
        
        trie = set()
        folders.sort(key=len)
        for folder in folders:
            path_list = folder.replace('/',' ').strip().split()
            i = 1
            while i <= len(path_list) and '/'+ '/'.join(path_list[:i]) not in trie:
                i += 1
            if i < len(path_list):
                continue
            else:
                i = 1
                trie.add(folder)
            
        return list(trie)





