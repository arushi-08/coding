class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        # [2,5,9]
        # [2,5]
        # [2,5] = closest to bounds
        # 
        bar_idx = {}
        left_traversal = []
        idx = 0
        for i, ch in enumerate(s):
            if ch == '|':
                bar_idx[i] = idx
                idx += 1
                left_traversal.append(i)
            elif left_traversal:
                left_traversal.append(left_traversal[-1])
            else:
                left_traversal = [len(s)]

        right_traversal = [len(s)] * len(s)

        for i in range(len(s)-1,-1,-1):
            if s[i] == '|':
                right_traversal[i] = i
            elif i < len(s) - 1:
                right_traversal[i] = right_traversal[i+1]

        ans = []
        for start, end in queries:
            if (
                (right_traversal[start] not in bar_idx) or 
                (left_traversal[end] not in bar_idx) or
                (bar_idx[right_traversal[start]] >= bar_idx[left_traversal[end]])
                ):
                ans.append(0)
            else:
                ans.append(
                    left_traversal[end] - right_traversal[start] - (bar_idx[left_traversal[end]] - bar_idx[right_traversal[start]]) 
                )

        return ans
