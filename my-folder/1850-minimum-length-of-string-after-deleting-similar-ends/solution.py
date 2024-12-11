class Solution:
    def minimumLength(self, s: str) -> int:
        '''
        pick non-empty prefix from string s where all chars in prefix are equal

        '''
        prefix = 0
        suffix = len(s)-1
        last_removed = ''
        while prefix < suffix:
            if s[prefix] == s[suffix]:
                last_removed = s[prefix]
                prefix += 1
                suffix -= 1
            elif s[prefix] == last_removed:
                prefix += 1
            elif s[suffix] == last_removed:
                suffix -= 1
            else:
                break
        
        if suffix == prefix and s[prefix] == last_removed:
            return 0
        return suffix - prefix + 1
