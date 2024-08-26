class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # hmap
        
        hset = set()

        for i in range(len(arr1)):
            arr1_element = str(arr1[i])
            for j in range(1,len(arr1_element)+1):
                hset.add(arr1_element[:j])
        
        longest_common_prefix = 0
        for i in range(len(arr2)):
            arr2_element = str(arr2[i])
            arr2_element_length = len(arr2_element)
            while (
                arr2_element_length and 
                arr2_element[:arr2_element_length] not in hset
                ):
                arr2_element_length -= 1
            if arr2_element[:arr2_element_length] in hset:
                longest_common_prefix = max(longest_common_prefix, arr2_element_length)
        
        return longest_common_prefix


