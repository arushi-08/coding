class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        # get min distance for each 0 cell to inf cell
        # bfs from gate, fill each empty cell with min step value
        # stop bfs when curr steps > existing cell value

        # put all gates in the queue
        # find nearby all inf cells
        # calculate distance

        queue = deque()
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue.append((i,j, 0))
        
        rows = [1,0,-1,0]
        cols = [0,1,0,-1]

        while queue:
            l = len(queue)
            for _ in range(l):
                currx, curry, dist = queue.popleft()

                for i in range(len(rows)):
                    if self.issafe(currx+rows[i], curry+cols[i], rooms, dist+1):
                        queue.append((currx+rows[i], curry+cols[i], dist+1))
                        rooms[currx+rows[i]][curry+cols[i]] = dist+1

    def issafe(self, x, y, rooms, dist):
        return 0 <= x < len(rooms) and 0 <= y < len(rooms[0]) and rooms[x][y] > dist
        

            



