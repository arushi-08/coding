class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        res = set()
        hmap = defaultdict(list)
        for i, t in enumerate(transactions):
            user, time, amount, city = t.split(',')
            hmap[user].append((int(time), city, i))
            if int(amount) > 1000:
                res.add(i)
        
        for k, v in hmap.items():
            v.sort()
            vlen = len(v)
            for i in range(vlen):
                old = v[i]
                for j in range(i+1, vlen):
                    new = v[j]
                    timediff = new[0] - old[0]
                    if timediff <= 60:
                        if new[1] != old[1]:
                            res.add(old[2])
                            res.add(new[2])
                    else:
                        break
        
        return [transactions[x] for x in res]
