class Solution:
    def permute(self, n: int) -> List[List[int]]:
        
        # given n
        # an alternating permutation = perm of first n +ve int such that no 2 adj elemnts are both odd or both even
        # return all such alternating perms sorted in lexicographical order

        # alternate 2nd degree numbers
        # get all permutations, if any 2 adj are odd or even: skip


        ans = []
        def dfs(i, ans, curr_permutation, used):
            if len(curr_permutation) == n:
                ans.append(curr_permutation)
                return
            
            for j in range(1, n+1):
                if ( (j & 1 != 0 and i & 1 == 0) or 
                    (j & 1 == 0 and i & 1 != 0) ) and j not in used:
                    used.add(j)
                    dfs(j, ans, curr_permutation + [j], used)
                    used.remove(j)

        used = set()
        for i in range(1,n+1):
            used.add(i)
            dfs(i, ans, [i], used)
            used.remove(i)
        
        return ans
