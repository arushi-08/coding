class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        # given s -> return num of unique palindroms of length 3 subsequence of s

        n = len(s)
        visited = defaultdict(list)

        for i in range(n):
            if s[i] in visited and len(visited[s[i]]) > 1:
                visited[s[i]][1] = i
                continue
            visited[s[i]].append(i)

        ans = 0
        for char in visited:
            if len(visited[char]) < 2:
                continue
            st, ed = visited[char]
            if ed - st < 2:
                continue
            for l in range(26):
                char = chr(ord('a')+l)
                if char in set(s[st+1:ed]):
                    ans += 1

        print('ans', ans)
        return ans

                    
