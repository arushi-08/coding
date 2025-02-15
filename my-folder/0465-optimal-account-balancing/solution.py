class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        
        # min transactions
        # 1 = 10
        # 2 = -5
        # 0 = -5
        # ans: 2
        balance = {}
        for transaction in transactions:
            from_, to_ , amount = transaction  
            balance[from_] = balance.get(from_, 0) - amount
            balance[to_] = balance.get(to_, 0) + amount
            if balance[from_] == 0:
                del balance[from_]
            if balance[to_] == 0:
                del balance[to_]

        balance_list = [x[1] for x in list(balance.items())]
        balance_list.sort()

        return self.backtrack(balance_list, 0)

    def backtrack(self, balance, neg_idx):
        
        n = len(balance) 

        while neg_idx < n and balance[neg_idx] == 0:
            neg_idx += 1

        if neg_idx == n:
            return 0

        ans = float('inf')

        for i in range(neg_idx+1, n):

            if balance[i] * balance[neg_idx] < 0:
                balance[i] += balance[neg_idx]
                ans = min(ans,
                    1 + self.backtrack(balance, neg_idx+1)
                )
                balance[i] -= balance[neg_idx]
        
        return ans
        


