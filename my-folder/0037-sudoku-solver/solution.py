class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # potential candidate digits
        # backtracking will be done

        # find potential
        # create a rowmap, colmap, cubemap
        # {1:{5,3,7}} potential are all other digits
        # before placing a number, check if it meets constraints, when constraints are met, put it as a temp value
        
        rowmap = defaultdict(set)
        colmap = defaultdict(set)
        cubemap = defaultdict(set)
        # cand_rowmap = defaultdict(list)
        # cand_colmap = defaultdict(list)
        # cand_cubemap = defaultdict(list)
        candidate_coordinates = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    rowmap[i].add(board[i][j])
                    colmap[j].add(board[i][j])
                    cubemap[(i//3, j//3)].add(board[i][j])
                else:
                    candidate_coordinates.append((i,j))
        def dfs(idx):
            # backtracking
            # check if coords will have 
            if idx == len(candidate_coordinates):
                return board 
            x,y = candidate_coordinates[idx]
            for i in range(1,10):
                if str(i) not in rowmap[x] and str(i) not in colmap[y] and str(i) not in cubemap[(x//3, y//3)]:
                    board[x][y] = str(i)
                    rowmap[x].add(str(i))
                    colmap[y].add(str(i))
                    cubemap[(x//3, y//3)].add(str(i))
                    ans = dfs(idx+1)
                    if ans:
                        return ans
                    rowmap[x].remove(str(i))
                    colmap[y].remove(str(i))
                    cubemap[(x//3, y//3)].remove(str(i))
            
        
        # for j in range(len(candidate_coordinates)):
        return dfs(0)
            
        
        return board

