class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:

        # given 2 arrs: instructions and values
        # start at the first instruction at index i=0
        visited = set()

        i = 0
        res = 0
        while 0 <= i < len(instructions):
            if i in visited:
                break
            visited.add(i)
            if instructions[i] == 'add':
                res += values[i]
                i += 1
            else:
                i += values[i]
            
        return res
