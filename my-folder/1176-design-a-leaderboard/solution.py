class Leaderboard:

    def __init__(self):
        self.leaderboard = {}
        
    def addScore(self, playerId: int, score: int) -> None:

        if playerId in self.leaderboard:
            score = self.leaderboard[playerId] + score
            
        self.leaderboard[playerId] = score

    def top(self, K: int) -> int:
        topkscore = 0
        heap = []
        for score in self.leaderboard.values():
            heappush(heap, -score)
        heapify(heap)

        while K:
            score = heappop(heap)
            topkscore += (-score)
            K -= 1

        return topkscore

    def reset(self, playerId: int) -> None:

        if playerId in self.leaderboard:
            oldscore = self.leaderboard[playerId]

        self.leaderboard[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
