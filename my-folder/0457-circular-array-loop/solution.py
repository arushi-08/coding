class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        
        # circular array
        # nums[i] + -> move forward
        # nums[i] - -> move backward

        # return true if there's a cycle in nums
        # else false

        #       2,-1,1,2,2 -> 
        #    0
        # idx = 2
        #          0
        #            3
        #              0
        #                1

        # does this relate to josephus problem?
        # try doing with fast_ptr and slow_ptr approach
        if not nums: return False

        def next_index(ptr):
            return (ptr + nums[ptr]) % n

        n = len(nums)

        for i in range(n):

            if nums[i] == 0:
                continue

            fast = i
            slow = i
            direction = nums[i] > 0

            while True:
                
                next_slow = next_index(slow)
                if nums[next_slow] == 0 or (nums[next_slow] > 0) != direction:
                    break
                slow = next_slow

                next_fast = next_index(fast)
                if nums[next_fast] == 0 or (nums[next_fast] > 0) != direction:
                    break
                fast = next_index(next_fast)
                if nums[fast] == 0 or (nums[fast] > 0) != direction:
                    break

                if slow == fast:
                    if slow == next_index(slow):
                        break
                    return True

            marker = i
            while nums[marker] != 0 and nums[marker] > 0 == direction:
                next_marker = next_index(marker)
                nums[marker] = 0
                marker = next_marker
            
        return False

        #   -2,1,-1,-2,-2
        # 0
        #   

            


