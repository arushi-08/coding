class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        
        bar_idx = []

        for i,ch in enumerate(s):
            if ch == '|':
                bar_idx.append(i)
        
        ans = []
        for i in range(len(queries)):
            left, right = queries[i]
            # print('left', left)
            # print('right', right)

            first_bar_on_left = self.lower_bound_search(bar_idx, left, 'LEFT')
            first_bar_on_right = self.lower_bound_search(bar_idx, right, 'RIGHT')
            
            # print('first_bar_on_left', first_bar_on_left)
            # print('first_bar_on_right', first_bar_on_right)

            if first_bar_on_left == -1:
                ans.append(0)
                continue
                
            if bar_idx[first_bar_on_right] > right:
                first_bar_on_right -= 1

            if left <= bar_idx[first_bar_on_right] and right >= bar_idx[first_bar_on_left]:
                res = bar_idx[first_bar_on_right] - bar_idx[first_bar_on_left] - (first_bar_on_right - first_bar_on_left)
            else:
                res = 0

            ans.append(res)
        
        return ans
    
    def lower_bound_search(self, bar_idx, left_query_bar, BAR_SIDE):

        start = 0
        end = len(bar_idx) - 1
        res = len(bar_idx)
        # print('enter')
        while start <= end:
            mid = (start + end) // 2
            if bar_idx[mid] >= left_query_bar:
                # print(bar_idx[mid], left_query_bar)
                res = min(mid, res)
                # print('res', res)
                end = mid - 1
            else:
                start = mid + 1
        
        if res == len(bar_idx):
            if BAR_SIDE == 'RIGHT':
                return res - 1
            return -1
        return res
    
