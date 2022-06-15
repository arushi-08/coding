class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
#         find smallest char > target
#           if char > target -> search in left space including target
#           if char <= target -> search in right space excluding target
#           while loop no equality
#           condition after loop

        left = 0
        right = len(letters)-1
        
        while left < right:
            mid = (left + right) // 2
            if letters[mid] > target:
                right = mid
            else:
                left = mid + 1
        
        if letters[left] > target:
            return letters[left]
        else:
            print("here", letters[left], target)
            return letters[0]
        
