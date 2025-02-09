class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:

        # given an int array groups where groups[i] represents size of ith group
        # given int array: elements
        # groups[i] % elements[j] == 0
        # o(n^2) can assign elements to each group
        # if group doesn't get assigned, check if it can be assigned with other nums
        # elements that are multiple of curr element will not get assigned

        # store trie of bits, 
        # 10 -  0110
        # 21 -  1011
        # 30 -  1111
        element_map = {}
        for i, element in enumerate(elements):
            if element in element_map:
                continue
            element_map[element] = i

        # element_map_items = list(element_map.items())

        def get_factors(group):
            limit = int(group**0.5)+1
            factors = []
            for i in range(1, limit):
                if group % i == 0:
                    factors.append(i)
                    factors.append(group//i)
            return factors
            
        result = []
        for group in groups:
            i = 0
            factors = get_factors(group)

            min_val = float('inf')
            for fact in factors:
                if fact in element_map:
                    min_val = min(min_val, element_map[fact])
        
            if min_val == float('inf'):
                result.append(-1)
            else:
                result.append(min_val)

        return result
