class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        # c[i] = count of nos that are present at or before index i in both A and B
        # prefix common array of A and B
        # 

        # at each idx, we have to check 2 new nos
        # use prev count + new idx elems
        # i=0, 1, 3
        # i=1, 3, 1
        # 2 sets - seta, setb
        # check in o(1)
        setab = set()
        # setb = set()
        ans = []
        for i in range(len(A)):
            
            count = 0
            if A[i] in setab or A[i] == B[i]:
                count += 1
            if B[i] in setab:
                count += 1
            if ans:
                ans.append(count + ans[-1])
            else:
                ans.append(count)
            setab.add(A[i])
            setab.add(B[i])

        return ans


