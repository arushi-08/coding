from heapq import heapify, heappop, heappush
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_rating = {}
        self.cuisines = {}
        self.food_cuisine = {}
        #O(NlogN)
        for f, c, r in zip(foods, cuisines, ratings): # O(N)
            self.food_rating[f] = r
            self.food_cuisine[f] = c
            if c not in self.cuisines:
                self.cuisines[c] = []
            heappush(self.cuisines[c], (-r, f)) # O(logN)

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_rating[food] = newRating # O(1)
        cuisine = self.food_cuisine[food]
        heappush(self.cuisines[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisines[cuisine]
        
        while heap and self.food_rating[heap[0][1]] != -heap[0][0]:
                heappop(heap)
                
        if heap:
            ans = heap[0][1]
        else:
            ans = -1
            
        return ans


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
