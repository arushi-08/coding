class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.board = [[0]*n for _ in range(n)]
        self.rowsum = [0]*n
        self.colsum = [0]*n
        self.diagsum = 0
        self.reverse_diagsum = 0

    def convert_player2(self, player):
        if player == -1:
            return 2
        if player == 2:
            return -1
        return player

    def move(self, row: int, col: int, player: int) -> int:
        # when player makes a move
        # update board, rowsum, colsum, diagsum, reverse_diagsum
        # check if any == n, return winner

        n = self.n
        player = self.convert_player2(player)
        # 0,0 | 0,1 | 0,1
        # 1,0   1,1
        self.board[row][col] = player
        self.rowsum[row] += player
        self.colsum[col] += player
        if row == col:
            self.diagsum += player
        if row == n - 1 - col:
            self.reverse_diagsum += player
        
        if abs(self.rowsum[row]) == n or abs(self.colsum[col]) == n or abs(self.diagsum) == n or abs(self.reverse_diagsum) == n:
            
            if player == -1:
                player = self.convert_player2(player)
            return player
        
        return 0






# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
