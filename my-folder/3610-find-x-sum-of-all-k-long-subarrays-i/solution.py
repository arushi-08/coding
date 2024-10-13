class Item:
    def __init__(self, k1, k2, val):
        self.k1 = k1
        self.k2 = k2
        self.val = val
    
    def __lt__(self, other):
        if self.k1 == other.k1:
            return self.k2 < other.k2
        else:
            return self.k1 < other.k1

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        
        # for each consecutive k nos
        # do top k heap
        ans = []
        for i in range(len(nums)-k+1):
            subnums = nums[i:i+k]
            # print('subnums', subnums, i, i+k, len(nums)-k+1)
            subnums_map = Counter(subnums)
            subnums = []
            for element in subnums_map:
                subnums.append(Item(-subnums_map[element], -element, element))
                # print('heap', -subnums_map[element], -element, element)
            heapify(subnums)
            
            j = 0
            curr_ans = 0
            while j < x:
                # print("j", j)
                if subnums:
                    item = heappop(subnums)
                    element = item.k2
                    freq = item.k1
                    # print(freq, element)
                    curr_ans += freq*element
                j += 1
            
            ans.append(curr_ans)
        
        return ans

