class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # find dup
        # o(1) time & space, and don't modify
        # 5, 4, 
        
        # o(n) space - hashmap/set
        # o(nlogn) time * o(1) space - sorting
        # 2 pointer?
        # linked list cycle find start point
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        st = nums[0]
        while st != slow:
            st = nums[st]
            slow = nums[slow]
        
        return st

