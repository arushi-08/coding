class Solution:
    def punishmentNumber(self, n: int) -> int:
        
        punishment_num = 0
        for i in range(1, n+1):
            if self.can_partition(i*i, i):
                punishment_num += i*i
        
        return punishment_num

    def can_partition(self, sq_num, num):
        
        if sq_num == num:
            return True
        
        if num < 0 or sq_num < num:
            return False
        
        return (
            self.can_partition(sq_num//10, num - sq_num % 10)
            or self.can_partition(sq_num//100, num - sq_num % 100)
            or self.can_partition(sq_num//1000, num - sq_num % 1000)
        )

        

        
