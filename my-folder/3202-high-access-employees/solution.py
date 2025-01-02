class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        
        # find high access employees
        # they access 3 or more times within an hour
        ans = []
        
        hmap = defaultdict(list)
        for emp, time in access_times:
            hmap[emp].append(int(time))
        
        for emp, times in hmap.items():
            if len(times)>2:
                times.sort()
                flag = False
                for i in range(len(times)-2):
                    flag |= times[i+2] - times[i] < 100
                if flag:
                    ans.append(emp)

        return ans

