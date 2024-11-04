class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        
        # string s
        # 2d array of integers queries, queries[i] = [li, ri]

        # for each query, how many same-end substrings are there
        # a - 1
        # bcaa - 5
        # caab - 5
        # abcaab - 10
        # 6
        # a-3 how many pairs with 3 chars - 3c2 - 3*2/2 - 3
        # b-2 - 2c2 - 1

        # outer loop on all queries - can think of skipping recomputation
        # for each query, calculate same end substrings
        
        dic = {}
        for c in set(s):
            dic[c] = [0] * (len(s) + 1)
        for i in range(1,len(s)+1):
            for char in dic:
                dic[char][i] = dic[char][i-1] + (1 if s[i-1] == char else 0)
                
        def get_count(query):
            count = 0
            left = query[0]
            right = query[1]
            for char in dic:
                fre = dic[char][right+1] - dic[char][left]
                count += fre * (fre-1)//2
            return count

        res = []

        for query in queries:
            count = query[1] - query[0] + 1 + get_count(query)
            res.append(count)

        return res

