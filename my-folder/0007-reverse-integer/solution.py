class Solution:
    def reverse(self, x: int) -> int:
        
        if x > 0:
            copy_x = x
        else:
            copy_x = -x
        # print(copy_x, str(copy_x))
        int_list = 0
        count = len(str(copy_x)) - 1
        while(copy_x>0):
            # print(copy_x%10)
            # print(pow(10,count))
            int_list += int(int(copy_x%10) * pow(10,count))
            copy_x /= 10
            count -= 1
        
        if int_list > pow(2, 31) - 1 or int_list < pow(-2, 31):
            return 0
        if x > 0:
            return int_list
        else:
            return -int_list
            
