class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
    
        # return min height
        # books are ordered
        # DP
        # return min(F(ht+1, bookwidth), F(ht, w+bookwidth))
        self.memo = {}
        return self.helper(0, 0, shelfWidth, shelfWidth,len(books), books)
    
    def helper(self, idx, height, remaining_width, shelfWidth, N, books):

        if idx == N:
            return height

        if (idx, height, remaining_width) in self.memo:
            return self.memo[(idx, height, remaining_width)]
        
        currwidth, currht = books[idx]

        # new line
        minht = self.helper(
            idx+1, currht, shelfWidth-currwidth, shelfWidth, N, books
        ) + height

        if currwidth <= remaining_width:
            min_ht_same_shelf = self.helper(
                idx+1, max(height, currht), 
                remaining_width-currwidth, shelfWidth, N, books
            )
            minht = min(minht, min_ht_same_shelf)

        self.memo[(idx, height, remaining_width)] = minht
        return self.memo[(idx, height, remaining_width)]
