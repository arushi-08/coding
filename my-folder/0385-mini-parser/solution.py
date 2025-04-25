# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        """
        use stack 
        [ -> store NestedInteger() in stack
        , -> i += 1
        ] -> pop from stack
        digit or - -> append to stack[-1]
        """
        if not s.startswith('['):
            return NestedInteger(int(s))
            
        stack = []
        current = None
        i = 0

        while i < len(s):
            if s[i] == '[':
                new_list = NestedInteger()
                # if stack:
                #     stack[-1].add(new_list)
                stack.append(new_list)
                i += 1

            elif s[i] == ',':
                i += 1
            
            elif s[i] == ']':
                current = stack.pop()
                if stack:
                    stack[-1].add(current)
                i += 1
            
            else:
                j = i
                while j < len(s) and (s[j].isdigit() or s[j] == '-'):
                    j += 1
                num = int(s[i:j])
                stack[-1].add(NestedInteger(num))
                i = j
        
        return current
        
