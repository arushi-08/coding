class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        # recursively

        # n = 1 -> return [1]
        # n = 2 -> return [[1,1]]

        # n = 3 -> add previous adj numbers

        # logic:
        # results = f(n-1)
        # create new list
        # iterate on the last results list
        # add adj elements of l_r_l
        # append 1 to sides

        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return self.generate(numRows-1) + [[1,1]]

        results = self.generate(numRows-1)

        last_result_val = results[-1]
        new_row_list = [1]

        for i in range(len(last_result_val)-1):
            new_row_list.append(last_result_val[i]+last_result_val[i+1])
        
        new_row_list.append(1)
        results.append(new_row_list)
        return results



