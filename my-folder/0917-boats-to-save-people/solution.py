class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort(reverse=True)

        csum = 0
        nboats = 0
        # 5,4,2,1
        ptr = len(people)-1
        i = 0
        # 5,4,3,3
        while i <= ptr:
            if csum + people[i] <= limit:
                csum += people[i]
            if i!=ptr and csum + people[ptr] <= limit:
                csum += people[ptr]
                ptr -= 1
            if csum <= limit:
                # print("csum", csum, "nboats", nboats)
                nboats += 1
                csum = 0
            i += 1

        if csum:
            return nboats + 1
        
        return nboats


