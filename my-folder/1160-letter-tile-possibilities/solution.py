class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        # n tiles
        # each tile has 1 letter tiles[i] printed on it
        # 
        def dfs(sequence, used, res):
            if len(sequence) == len(tiles):
                return

            for j in range(len(tiles)):
                new_seq = sequence+tiles[j]
                if j not in used:
                    used.add(j)
                    res.add(new_seq)
                    dfs(new_seq, used, res)
                    used.remove(j)

        used = set()
        res = set()
        for i in range(len(tiles)):
            used.add(i)
            res.add(tiles[i])
            dfs(tiles[i], used, res)
            used.remove(i)
        # print(res)
        return len(res)

