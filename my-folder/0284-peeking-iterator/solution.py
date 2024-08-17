# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = []
        while iterator.hasNext():
            self.iterator.append(iterator.next())
        self.idx = 0
        # print('self.iterator', self.iterator)

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.idx < len(self.iterator):
            return self.iterator[self.idx]
        return -100000

    def next(self):
        """
        :rtype: int
        """
        if self.idx < len(self.iterator):
            ans = self.iterator[self.idx]
            self.idx += 1
            return ans
        return -100000
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.idx < len(self.iterator):
            return True
        return False

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
