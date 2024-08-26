from functools import lru_cache
class Solution:
    def get_all_perfect_squares(self, sq_num):
        squares = []
        while sq_num:
            if (sq_num ** 0.5).is_integer():
                squares.append(sq_num)
            sq_num -= 1
        return squares

    def numSquares(self, n: int) -> int:
        
        squares = self.get_all_perfect_squares(n)
        # got all perfect squares
        # print(squares)
        memo = {}
        return self.helper(n, squares, 0, memo)

    def helper(self, n, squares, idx, memo):
        # return min coins that make up n
        # knapsack    
        if n == 0:
            return 0
        
        if n < 0 or idx == len(squares):
            return float('inf')

        if (n, idx) in memo:
            return memo[(n, idx)]

        memo[(n, idx)] = min(
            self.helper(n-squares[idx], squares, idx, memo) + 1,
            self.helper(n, squares, idx+1, memo)
        )
        return memo[(n, idx)]


