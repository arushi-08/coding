class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        # child w higher rating gets more candy than neighbor
        # 2,1,2
        # 1,2,1

        # if child i has higher rating > i+1
        # more candy > i+1
        # keep dec stack
        # when i < i + 1 found, assign i the least candies
        # and all prev elems, +1
        # 1, 0, 2
        # 1- append to stack
        # 0- assign candy = 1, pop stack, candy + 1 for 1 => 2
        # 2- candy + 1 => 2

        candies = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1]+1
        
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
                candies[i] = candies[i+1] + 1
        print('candies', candies)
        return sum(candies)
