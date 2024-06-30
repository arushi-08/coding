class SparseVector:
    def __init__(self, nums: List[int]):
        self.vector = {}
        for i, num in enumerate(nums):
            if num:
                self.vector[i]=num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        if len(self.vector) > len(vec.vector):
            for k in self.vector:
                ans += self.vector[k] * vec.vector.get(k, 0)
        else:
            for k in vec.vector:
                ans += vec.vector[k] * self.vector.get(k, 0)
            
        return ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
