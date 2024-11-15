from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.tmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tmap: return ""
        kmap = self.tmap[key]

        st = 0
        ed = len(kmap)-1
        maxt = ""
        while st <= ed:
            mid = (st + ed)//2
            if kmap[mid][0] <= timestamp:
                maxt = kmap[mid][1]
                st = mid + 1
            else:
                ed = mid - 1
        
        return maxt



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
