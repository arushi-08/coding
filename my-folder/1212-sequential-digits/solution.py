class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        """
        convert low to string
        iterate on string?
        keep adding sequential digit to element till you reach value > low
        update low to current value

        """
        string = "123456789"
        n = 10
        ans = []

        for length in range(len(str(low)), len(str(high))+1):
            for start in range(n-length):
                nums = int(string[start:start+length])
                if nums >= low and nums <= high:
                    ans.append(nums)
        
        return ans
