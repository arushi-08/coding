class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        
        n = len(s)
        memo = {}
        begin = -1
        if s[0] == '*':
            psum = [1]
        else:
            psum = [0]
        for i in range(1,len(s)):
            if s[i] == '*':
                psum.append(psum[-1] + 1) 
            else:
                psum.append(psum[-1])
        
        leftcandlecount = [-1] * (n)
        for i in range(n):
            if s[i] == '|':
                leftcandlecount[i] = i
            else:
                leftcandlecount[i] = leftcandlecount[i-1]

        rightcandlecount = [-1] * (n)
        for i in range(n-1,-1,-1): 
            if s[i] == '|':
                rightcandlecount[i] = i
            else:
                if i == n-1:
                    continue
                rightcandlecount[i] = rightcandlecount[i+1]

        
        ans = []
        for query in queries:
            left, right = query
            leftcandleidx = rightcandlecount[left]
            rightcandleidx = leftcandlecount[right]

            # print("rightcandleidx", rightcandleidx, psum[rightcandleidx])
            # print("leftcandleidx", leftcandleidx, psum[leftcandleidx])

            if rightcandleidx >= left and right >= leftcandleidx:
                count = psum[rightcandleidx] - psum[leftcandleidx]
            else:
                count = 0
            ans.append(count)
        
        return ans
