class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        
        # given 2 strings s and goal
        # true if can swap 2 letters in s and s = goal
        # else false

        if len(s) != len(goal): return False
        s_list = list(s)
        g_list = list(goal)
        mismatched_idx = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                if mismatched_idx:
                    s_list[i], s_list[mismatched_idx[0]] = s_list[mismatched_idx[0]], s_list[i]
                    if s_list == g_list:
                        return True
                    return False

                else:
                    mismatched_idx.append(i)
        
        if not mismatched_idx:
            s_freq = {}
            for i in s:
                if i in s_freq:
                    return True
                s_freq[i] = 1
                
        return False
        
