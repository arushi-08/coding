class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        
        bin_x = self.convert_to_binary(x)
        bin_y = self.convert_to_binary(y)
        
        min_length = min(len(bin_y), len(bin_x))
        
        ans = 0
        for i in range(1, min_length+1):
            
            # if i > min_length:
                # break
            
            if bin_y[-i] != bin_x[-i]:
                print(bin_y[-i], bin_x[-i])
                ans += 1
        
        if len(bin_y) > len(bin_x):
            list_y = list(bin_y[:-min_length])
            ans += sum([int(i) for i in list_y])
            print(ans)
        
        elif len(bin_x) > len(bin_y):
            list_x = list(bin_x[:-min_length])
            ans += sum([int(i) for i in list_x])
            
        return ans
        
                
        
        
    def convert_to_binary(self, x):
        
        if x == 0:
            return '0'
        ans = []
        
        while (x > 0):
            
            ans.insert(0, str(int(x%2)))
            x = int(x/2)
        
        return "".join(ans)
