class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        # 4 int sep by single dots
        # 0-255
        # no leading zeros

        # return all possible valid ip addresses

        # similar to decode ways

        if s == '0000':
            return ['0.0.0.0']

        def dfs(i, result, res):
            if res.count('.') == 3 and i == len(s):
                result.append(res)
                return
            
            if res.count('.') == 3 and i + 3 < len(s):
                return

            for j in range(1,4):
                if s[i:i+j] and int(s[i:i+j]) < 256 and i+j <= len(s):
                    if s[i] == '0' and j > 1:
                        return
                    print(s[i:i+j], s[i], s[j-1])
                    if not res:
                        dfs(i+j, result, res+s[i:i+j])
                    else:
                        dfs(i+j, result, res+'.'+s[i:i+j])


        # 25525511135
        result = []
        dfs(0, result, '')
        return result

