class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        # backtracking
        # iterate on the word
        # 2 choices:
        # f(not include curr word[i], count + 1)
        # curr abbrv += count
        # reset count
        # f(include curr word[i], count)


        ans = []
       
        def dfs(word, idx, curr_abbrv, count):
            if idx == len(word):
                if count:
                    curr_abbrv += str(count)
                ans.append(curr_abbrv)
                return
            
            dfs(word, idx+1, curr_abbrv, count+1)
            if count:
                curr_abbrv += str(count)
                count = 0
            dfs(word, idx+1, curr_abbrv+word[idx], count)

        dfs(word, 0, '', 0)

        return ans
        



