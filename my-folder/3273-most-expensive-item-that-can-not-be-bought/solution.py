class Solution:
    def mostExpensiveItem(self, primeOne: int, primeTwo: int) -> int:
        
        # prime nums can repeat
        # make set of cannot make elements
        # break down each price into smaller elements < largest element in set
        #   if all of the smaller elements are not in set (can be made)
        #   element can be made
        #   elif any smaller element cannot be made -> element cannot be made
        #          add it to set, set it as maxprice


        return primeOne * primeTwo - primeOne - primeTwo
