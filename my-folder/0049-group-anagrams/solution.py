from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        answer = []
        temp_dict = defaultdict(list)
        for i in range(len(strs)):
            temp_dict[tuple(sorted(strs[i]))].append(strs[i])
            
        for key, val in temp_dict.items():
            answer.append(val)
        return answer

