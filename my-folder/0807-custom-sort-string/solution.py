class Solution:
    def customSortString(self, order: str, s: str) -> str:
        

        custom_order = {}
        
        for i, o in enumerate(order):
            custom_order[o] = i
        
        def custom_sort(x):
            return custom_order.get(x, float('inf'))
        
        return ''.join(sorted(s, key=custom_sort))
