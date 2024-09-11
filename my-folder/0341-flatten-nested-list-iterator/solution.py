# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nested_list: [NestedInteger]):
        self.flattened = self.flatten_generator(nested_list)
        try:
            self.next_integer = next(self.flattened)
        except StopIteration:
            self.next_integer = None
    
    def flatten_generator(self, nested_list):
        for i in range(len(nested_list)):
            if nested_list[i].isInteger():
                yield nested_list[i]
            else:
                yield from self.flatten_generator(nested_list[i].getList())
    
    def next(self) -> int:
        next_integer = self.next_integer
        try:
            self.next_integer = next(self.flattened)
        except StopIteration:
            self.next_integer = None

        return next_integer
    
    def hasNext(self) -> bool:
        return self.next_integer is not None

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
