class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        shuffled_str = [""]*len(s)
        for idx, character in enumerate(s):
            shuffled_str[indices[idx]] = character
        
        return "".join(shuffled_str)
