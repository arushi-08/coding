class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        
        # given pal string, replace exactly one char with any lowercase english letter
        # so that resulting str is not a pal and it's lexicographically smallest one possible

        # to make smallest possible
        # start from left to right
        # replace char with 'a'

        pal_list = list(palindrome)

        """3 condns: 
        find 1st pos where char is not a
            if left and right of this char are not same: return [:i] + 'a' + [i+1:]
        if pal length > 1:
            return [:-1] + 'b'
        return ''
        """
        for i in range(len(pal_list)):
            if pal_list[i] != 'a':
                if pal_list[:i] != pal_list[i+1:]:
                    return ''.join(pal_list[:i]) + 'a' + ''.join(pal_list[i+1:])
        
        if len(pal_list) > 1:
            return ''.join(pal_list[:-1]) + 'b'
        return ''
