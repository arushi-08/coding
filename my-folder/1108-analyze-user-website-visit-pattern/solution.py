class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        # given 2 string arrays username and website
        # integer array timestamp
        # all the given arrays are of the same length and tuple 
        # [usernamei, websitei, timestampi]
        # pattern is a list of 3 websites

        # [home, away, love], [leetcode, love, leetcode]
        # [luffy, luffy, luffy]
        # 

        # score of pattern = num of users that visited all websites in pattren
        # in same ordered they appeared in the pattern

        # [home, away, love] -> score is num of uesrs x, x visited home then away then love

        # return pattern with highest score

        # create tuples
        # same websites,
        # home - 1, 4, 7, 8
        # about - 2, 9,
        # career - 3, 10
        # 
        # joe -> home, about, career
        # james -> home, cart, maps, home
        # mary -> home, about, career

        # iterate on people
        # store possible 3 contiguous arrays
        # return the most frequent contiguous array
        webvisits = []
        for time, user, site in zip(timestamp, username,  website):
            webvisits.append([time, site, user])
        webvisits.sort()

        graph = defaultdict(list)
        for time, site, user in webvisits:
            graph[user].append(site)
        
        pattern_freq = defaultdict(set)
        for user, sites in graph.items():
            for i in range(len(sites)):
                for j in range(i+1, len(sites)):
                    for k in range(j+1, len(sites)):
                        pattern_freq[(sites[i], sites[j], sites[k])].add(user)
            
        max_users = 0
        popular_pattern = []
        for k, v in pattern_freq.items():
            if len(v) > max_users:
                max_users = len(v)
                popular_pattern = list(k)
            elif len(v) == max_users:
                popular_pattern = sorted([popular_pattern, list(k)])[0]
        return popular_pattern


        

