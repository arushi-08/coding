class Solution:
    def hIndex(self, citations: List[int]) -> int:
        

        # max h such that there are h papers, that have atleast h citations
        # hmap: {citation count: how many times + 1 if greater citation count exists}
        
        # break down the problem
        # max h such that there are h papers with atleast h citations
        # binary search

        if len(citations) == 1 and citations[0]:
            return 1

        start = 0
        end = len(citations)
        max_h_index = 0
        # [3,0,6,1,5]
        # search space: 0, 1, 2, 3, 4, 5
        while start <= end:
            mid = (start + end) // 2

            if self.h_index_possible(mid, citations):
                max_h_index = max(max_h_index, mid)
                start = mid + 1
            else:
                end = mid - 1

        return max_h_index

        
    def h_index_possible(self, h_index, citations):

        count = 0
        for citation in citations:
            if citation >= h_index:
                count += 1
        
        return count >= h_index


