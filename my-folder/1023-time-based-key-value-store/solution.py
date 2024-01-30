from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        item = self.timemap[key]
        # if timestamp in item:
        #     return item[timestamp]
        
        # sorted_items = dict(sorted(item.items(), key=lambda x:x[0]))
        
        if not item:
            return ""
        if item[0][0] > timestamp:
            return ""
        
        left = 0
        right = len(item)-1
        res = ""
        while left <= right:
            mid = (left + right)//2
            if item[mid][0] <= timestamp:
                res = item[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return res

        # love: 10: high, 20: low
        # love : 5 -> ""
        # love : 10 -> high
        # love : 15 -> HIGH


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
