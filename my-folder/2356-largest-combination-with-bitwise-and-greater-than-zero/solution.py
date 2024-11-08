class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        # bitwise AND of array
        # every candidate is 24 bits long
        # so for every bit position
        #   calculate size of largest combination
        #   such that bitwise AND will have a 1 in that bit position

        # 16
        # 00000000000010000
        # for every position calculate size of largest combination
        
        candidate_strings = []
        for number in candidates:
            candidate_strings.append(bin(number)[2:].zfill(24))

        maxcount = 0
        for i in range(24):
            count = 0
            for j in range(len(candidates)):
                # print(len(candidates[j]))
                if candidate_strings[j][i] == '1':
                    count += 1
            
            maxcount = max(maxcount, count)
        
        return maxcount
                


        # ands = 1
        # maxcount = 0

        # def dfs(ands,i,count):
        #     nonlocal maxcount

        #     if i == len(candidates):
        #         # print('count',count)
        #         maxcount = max(maxcount, count)
        #         return
            
        #     for j in range(i, len(candidates)):
        #         if i == 0:
        #             ands = candidates[j]

        #         if ands & candidates[j] > 0:
        #             ands &= candidates[j]
        #             # print(ands, count)
        #             dfs(ands,j+1,count+1)
                
                
        # dfs(ands,0, 0)
        
        # return maxcount


