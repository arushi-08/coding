class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        
        # alice is texting bob using her phone
        # mapping of digits to letters is shown in the figure below

        # pressed_keys = '22233'
        # return total number of possible text msgs alice could have sent

        # can't do backtracking
        digit_map = {'2':'a','22':'b','222':'c','3':'d','33':'e','333':'f','4':'g','44':'h','444':'i','5':'j','55':'k','555':'l','6':'m','66':'n','666':'o','7':'p','77':'q','777':'r','7777':'s','8':'t','88':'u','888':'v','9':'w','99':'x','999':'y','9999':'z'}
        memo = [-1] * (len(pressedKeys) + 1)
        def dfs(idx):
            if idx == len(pressedKeys):
                return 1
            
            if idx > len(pressedKeys):
                return 0

            if memo[idx] != -1:
                return memo[idx]

            ans = 0
            for i in range(1,5):
                if pressedKeys[idx:idx+i] in digit_map:
                    ans += dfs(idx+i)
            memo[idx] = ans % (10**9+7)
            return ans % (10**9+7)
        
        ans = dfs(0)
        # print(memo)
        return ans 


