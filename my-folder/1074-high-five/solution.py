class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        
        items.sort(key=lambda x: (x[0], x[1]), reverse=True)

        result_dict = defaultdict(list)

        for i in range(len(items)):
            if items[i][0] not in result_dict or len(result_dict[items[i][0]]) < 5:
                result_dict[items[i][0]].append(items[i][1])
        
        result = []

        for key in result_dict:
            result.append([key, sum(result_dict[key])//5])
        
        result.sort()

        return result
        
           

