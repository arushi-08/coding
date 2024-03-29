class Solution:
    def countArrangement(self, n: int) -> int:
        
        if n == 1: return 1

        # how to get all permutations of 1 to n integers
        # for every index of the permutation
        # either perm[i] % i or i % perm[i]
        perms = []

        def check(res):
            for j in range(1,len(res)+1):
                if res[j-1] % j and j % res[j-1]:
                    return False
            return True

        def get_permutations(res):
            if len(res) == n:
                perms.append(res.copy())
                return 
            
            for i in range(1, n+1):
                if i not in res:
                    res.append(i)
                    if not check(res): 
                        res.pop()
                        continue
                    get_permutations(res)
                    res.pop()

        get_permutations([])

        ans = len(perms)
        # for i in range(len(perms)):
        #     for j in range(1,n+1):
        #         if perms[i][j-1] % j and j % perms[i][j-1]:
        #             return False
        #     return True
        return ans
    
