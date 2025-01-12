class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        
        # circular arr
        # find cycle in arr

        # slow and fast pointer?

        # [2,-1,1,2,2]

        # start at 0
        # 2 steps forward -> idx 2
        # 1 step f -> idx 3
        # 2 step f -> idx 5 % 5 = 0 -> cycle

        # 0 2 3 0
        # slow = 0, fast = 0
        # 2, 3
        # 3, 2
        # 0, 0

        def move_ptrs(slow, fast):
            visited_idx.add(slow)
            visited_idx.add(fast)

            slow = (len(nums) + nums[slow] + slow) % n
            fast = (len(nums) + nums[fast] + fast) % n
            if nums[slow] * nums[fast] < 0:
                return -1, -1
            fast = (len(nums) + nums[fast] + fast) % n
            if nums[slow] * nums[fast] < 0:
                return -1, -1
            return slow, fast
           
        n = len(nums)
        
        visited_idx = set()
        
        for i in range(n):
            if i in visited_idx:
                continue

            slow = i
            fast = i
            
            while nums[slow] * nums[fast] > 0:
                
                inside = True
                slow, fast = move_ptrs(slow, fast)
                if slow == -1: 
                    break

                if slow == fast:
                    slow, fast = move_ptrs(slow, fast)
                    if slow == -1 or slow == fast:
                        break
                    else:
                        return True

        return False





