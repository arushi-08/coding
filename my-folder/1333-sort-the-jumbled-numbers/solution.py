class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        
        # sort acc to mapping (digit)
        # if same rank, keep nums order

        def sort_acc_to_mapping(num1, num2):
            nonlocal newnums
            newnum1 = newnums[num1]
            newnum2 = newnums[num2]
            
            return newnum1 - newnum2

        def get_new_num(num):
                newnum = 0
                exp = 0
                if num == 0:
                    newnum = mapping[num]
                else:
                    while num:
                        num, digit = divmod(num, 10)
                        newnum += mapping[digit] * 10**exp
                        exp += 1
                return newnum

        newnums = {}
        for num in nums:
            newnums[num] = get_new_num(num)

        nums.sort(key=cmp_to_key(sort_acc_to_mapping))
        return nums
