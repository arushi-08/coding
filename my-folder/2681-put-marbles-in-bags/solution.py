class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        
        # return max - min scores
        # divide marbles into k bags
        # no bag is empty
        # ith marble and jth marble are in a bag
        #   all marbles with an index between ith and jth idx should also be in that same bag
        # if a bag consists of all marbles with an index from i to j
        # cost = weights[i] + weights[j]
        # break points = k+1
        # start and end are same -> diff break points = k-1
        # make k-1 breaks in weights arr
        # how do i make k-1 breaks
        # 1 break at i is weights[i] + weights[i+1]
        # find max ( weights[i] + weights[i+1] ) k times
        # put it in heap
        if len(weights) <= 2 or k == 1:
            return 0

        max_score_heap = []
        for i in range(len(weights)-1):
            heappush(max_score_heap, weights[i] + weights[i+1] )
            if len(max_score_heap) > k-1:
                heappop(max_score_heap)
        
        max_score_val = sum(max_score_heap)


        min_score_heap = []
        for i in range(len(weights)-1):
            heappush(min_score_heap, -(weights[i] + weights[i+1]) )
            if len(min_score_heap) > k-1:
                heappop(min_score_heap)
        
        min_score_val = -sum(min_score_heap)

        return max_score_val-min_score_val
