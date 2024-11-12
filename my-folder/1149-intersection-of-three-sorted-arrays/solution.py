class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        
        intersection = []

        i = 0
        j = 0
        k = 0
        while i < len(arr1) and j < len(arr2) and k < len(arr3):
            if arr1[i] == arr2[j] == arr3[k]:
                intersection.append(arr1[i])
                i += 1
                j += 1
                k += 1
                continue
            
            min_num = min(arr1[i], arr2[j], arr3[k])
            if arr1[i] == min_num:
                i += 1
            if arr2[j] == min_num:
                j += 1
            if arr3[k] == min_num:
                k += 1
            
        
        return intersection


            

