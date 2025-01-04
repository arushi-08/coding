class Solution:

    def __init__(self, m: int, n: int):
        self.matrix = {}
        self.start = 0
        self.end = m*n-1
        self.n = n

    def flip(self) -> List[int]:
        val = random.randint(self.start, self.end)
        res = self.matrix.get(val, val)
        self.matrix[val] = self.matrix.get(self.start, self.start)
        self.start += 1
        # 3*4 0 1 2 3 4 5 6 7
        return [res//self.n, res%self.n]

    def reset(self) -> None:
        self.matrix = {}
        self.start = 0

# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()
