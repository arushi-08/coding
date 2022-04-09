class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(len(board)):
            int_list = [str(m) for m in range(10)]
            
            for j in range(len(board[0])):
                
                if board[i][j] != ".":
                    if str(board[i][j]) in int_list:
                        int_list[int_list.index(board[i][j])] = -1
                    else:
                        
                        return False
            
            int_row_list = [str(m) for m in range(10)]
            for k in range(len(board[0])):  
                if board[k][i] != ".":
                    if str(board[k][i]) in int_row_list:
                        int_row_list[int_row_list.index(board[k][i])] = -1
                    else:
                        
                        return False
        
        
        for i in range(0, 9, 3):
            for m in range(0, 9, 3):
                int_box_list = [str(m) for m in range(10)]
                for j in range(3):
                    for k in range(3):
                        # print("check iteration", j+i, k+m)
                        if board[j+i][k+m] != ".":
                            if str(board[j+i][k+m]) in int_box_list:
                                # print(str(board[j+i][k+m]), j+i, k+m)
                                int_box_list[int_box_list.index(board[j+i][k+m])] = -1
                            else:
                                # print(int_box_list)
                                # print(str(board[j+i][k+m]), j+i, k+m)
                                # print(str(board[j+i][k+m]) in int_box_list)
                                return False

        return True
