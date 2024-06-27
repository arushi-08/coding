class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
    
        #  a transaction is invalid if amount > 1000
        # if it occurs within 60 min and in another city

        tmap = defaultdict(list)
        invalid = set()
        for i, t in enumerate(transactions):
            name, time, amount, city = t.split(',')
            tmap[name].append((int(time) ,i, city))
            if int(amount) > 1000:
                invalid.add(i)
            
        # print("tmap", tmap)
        for k,v in tmap.items():
            v.sort()
            print(k)
            print(v)
            for i in range(len(v)):
                timei, idxi, cityi = v[i]
                for j in range(i+1, len(v)):
                    timej, idxj, cityj = v[j]
                    # print("idxi", idxi, idxj, timei, timej)
                    if timej - timei <= 60:
                        if cityj != cityi:
                            invalid.add(idxi)
                            invalid.add(idxj)
                    else:
                        break
        
        ans = []
        for i in invalid:
            ans.append(transactions[i])

        return ans
                    
        
        

