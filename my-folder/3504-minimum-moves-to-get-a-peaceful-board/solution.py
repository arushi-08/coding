class Solution:
    def minMoves(self, rooks: List[List[int]]) -> int:
        # big brain concept: sorting isn't actually moving the rooks to any other position
        # it just helps us get the min distance that rook has to move (either horizontally or vertically)
        #   by that i mean : abs(i - rooks[i][0])
        # greedy soln:
        # sort rooks by rows
        #   distribute on all rows
        #       sort rooks by columns
        #           distribute on all columns

        rooks.sort(key=lambda x: x[0])
        n_steps = 0
        for i in range(len(rooks)):
            n_steps += abs(i - rooks[i][0])
            rooks[i][0] = i
        
        rooks.sort(key=lambda x: x[1])

        for i in range(len(rooks)):
            n_steps += abs(i - rooks[i][1])
            rooks[i][1] = i
        
        return n_steps
