from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        email_hmap = defaultdict(list)
        email_to_name_hmap = {}
        for i in range(len(accounts)):
            name = accounts[i][0]
            
            if len(accounts[i]) == 2:
                email = accounts[i][1]
                email_hmap[email] = []
                email_to_name_hmap[email] = name
                continue
            for j in range(1, len(accounts[i])):
                for k in range(1, len(accounts[i])):
                    if j==k:
                        continue
                    email = accounts[i][j]
                    email_hmap[email].append(accounts[i][k])
                email_to_name_hmap[email] = name
        
        # do dfs on adjacency list email_hmap
        visited = set()
        def dfs(key, res):
            if key not in email_hmap:
                return
            
            for i in range(len(email_hmap[key])):
                next_email = email_hmap[key][i]
                if next_email not in visited:
                    res.append(next_email)
                    visited.add(next_email)
                    dfs(next_email, res)
        
        email_hmap_dfs = {}
        for k, v in email_hmap.items():
            res = []
            if k not in visited:
                visited.add(k)
                dfs(k, res)
                email_hmap_dfs[k] = res

        # print("email_hmap", email_hmap)
        # print("-")
        # print("email_hmap_dfs", email_hmap_dfs)
        ans = []
        for k, v in email_hmap_dfs.items():
            name = email_to_name_hmap[k]
            emails = sorted([k] + v)
            ans.append([name] + emails)
        
        return ans

                
                
