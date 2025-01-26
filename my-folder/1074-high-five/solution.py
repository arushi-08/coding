class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:

        result_dict = defaultdict(list)

        for i in range(len(items)):
            heappush(result_dict[items[i][0]], items[i][1])
            
            if len(result_dict[items[i][0]]) > 5:
                heappop(result_dict[items[i][0]])
        
        result = []

        for key in result_dict:
            result.append([key, sum(result_dict[key])//5])
        
        result.sort()

        return result
        
           

