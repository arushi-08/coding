class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        if len(nums)==1: return True
        return self.helper(True, nums, 0, len(nums)-1, 0, 0)
    
    def helper(self, player1_turn, nums, st, ed, p1_score, p2_score):
        if st == ed:
            if player1_turn:
                return p1_score + nums[st] >= p2_score
            return p1_score >= p2_score + nums[st]
        
        if player1_turn:
            a = self.helper(False, nums, st+1, ed, p1_score+nums[st], p2_score)
            b = self.helper(False, nums, st, ed-1, p1_score+nums[ed], p2_score)
            return a or b
        
        a = self.helper(True, nums, st+1, ed, p1_score, p2_score+nums[st])
        b =  self.helper(True, nums, st, ed-1, p1_score, p2_score+nums[ed])
        return a and b



