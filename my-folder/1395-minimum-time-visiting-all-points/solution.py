class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        
        time = 0
        for i in range(len(points)-1):
            start_x, start_y = points[i]
            end_x, end_y = points[i + 1]
            # print(start_x, end_x)
            while start_x != end_x and start_y != end_y:
#                 keep moving diagonally till reach same row/col as end point
                if abs(end_x - start_x) < abs(end_y - start_y):
                    time += abs(end_x - start_x)
                        
                    if end_y > start_y:
                        start_y += abs(end_x - start_x)
                    else:
                        start_y -= abs(end_x - start_x)
                    
                    if end_x > start_x:
                        start_x += abs(end_x - start_x)
                    else:
                        start_x -= abs(end_x - start_x)
                        
                else:
                    time += abs(end_y - start_y)
                    
                    if end_x > start_x:
                        start_x += abs(end_y - start_y)
                    else:
                        start_x -= abs(end_y - start_y)
                        
                    if end_y > start_y:
                        start_y += abs(end_y - start_y)
                    else:
                        start_y -= abs(end_y - start_y)
                
                print(start_x, start_y)
                
            if start_x == end_x:
                time += abs(end_y - start_y)
            else:
                time += abs(end_x - start_x)
                
        return time
            
    
