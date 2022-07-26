class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        prev = None
        people = []
        for i, seat in enumerate(seats):
            if seat:
                people.append(i)
        
        people = iter(people)
        future = next(people, None)
        ans = 0
        for i in range(len(seats)):
            if seats[i]:
                prev = i
            else:
                while future is not None and future < i:
                    future = next(people, None)
                
                if prev is None:
                    left_distance = float("inf")
                else:
                    left_distance = i - prev
                
                if future is None:
                    right_distance = float("inf")
                else:
                    right_distance = future - i
                
                ans = max(ans, min(left_distance, right_distance))
        
        return ans
                    
                    
                    
                    
