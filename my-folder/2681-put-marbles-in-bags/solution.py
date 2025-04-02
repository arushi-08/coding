class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        
        # k bags
        # given 0 indexed integer array weights
        # where weights[i] is wt of ith marble

        # given int k

        # divide the marbles into k bags based on rules:

        # no bag is empty
        # marbles[i:j+1] in same bag
        # cost of bag is wts[i] + wts[j]
        # score = sum of all costs
        # return diff between max and min scores among marble distributions

        # max score when maxwt is at boundary
        # min score when maxwt is not at boundary
        # find subarray end points
        # if there are k bags
        # then 2*k boundary points (but when they are overlappings, its actually k+1 points, 2 of these are the corner points that will always be there, so find for k-1 points) _ _ _
        
        if len(weights) == k: return 0

        # put k-1 points
        # assume sum till now is x, if we put another partition at index j, sum is x + A[j] + A[j+1]
        # top k-1 breaks
        # 

        # MAX(sum of k-1 adj pairs) - MIN(sum of k-1 adj pairs)
        # wts[i] + wts[i+1], compute these for each adjacent pair
        # how to compute this?

        if k == 1: return 0

        max_sigma = self.get_max_sigma(weights, k)
        min_sigma = self.get_min_sigma(weights, k)
        return max_sigma - min_sigma
    
    def get_max_sigma(self, weights, k):
        "sum of top k-1 elements"
        heap = []
        for i in range(len(weights)-1):
            newelem = weights[i] + weights[i+1]
            if len(heap) == k-1: 
                if heap[0] < newelem:
                    heappop(heap)
                    heappush(heap, newelem)
            else:
                heappush(heap, newelem)
        
        # heap has top k-1 points
        return sum(heap)
    
    def get_min_sigma(self, weights, k):
        "sum of bottom k numbers"
        heap = []
        for i in range(len(weights)-1):
            newelem = weights[i] + weights[i+1]
            if len(heap) == k-1: 
                if -heap[0] > newelem:
                    heappop(heap)
                    heappush(heap, -newelem)
            else:
                heappush(heap, -newelem)
        
        # heap has bottom k-1 points
        return -sum(heap)


                

                








