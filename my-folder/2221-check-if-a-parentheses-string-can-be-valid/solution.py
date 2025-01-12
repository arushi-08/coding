class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        
        # parenthesis is valid when ('s > ) and by the end they are same
        # maintain 2 balances
        # decrease balances when ) & locked, increase balances when ( & locked
        # inc max balance and dec min balance when unlocked
        # if max balance < 0 -> invalid
        # finally, if min balance == 0 -> valid else invalid
        
        if len(s) & 1: return False
        stack = []
        max_balance = 0
        min_balance = 0
        i = 0
        while i < len(s):
            if s[i] == ')':
                if locked[i] == '1':
                    max_balance -= 1
                    min_balance -= 1
            else:
                if locked[i] == '1':
                    max_balance += 1
                    min_balance += 1
            if locked[i] == '0':
                    max_balance += 1
                    min_balance -= 1
            min_balance = max(0, min_balance)
            if max_balance < 0:
                return False
            i += 1
        
        if min_balance == 0:
            return True
        
        return False
