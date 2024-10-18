class Solution:
    def maximumSwap(self, num: int) -> int:
        # swap 2 digits at most once
        # swap largest element to 1st position

        num_list = list(str(num))
        i = len(num_list)-1
        stack = [len(num_list)-1]
        
        while i >= 0:
            if num_list[i] > num_list[stack[-1]]:
                stack.append(i)
            i -= 1
        
        small_idx= -1
        for i in range(len(num_list)):
            if num_list[i] < num_list[stack[-1]]:
                small_idx = i
                break
            if i >= stack[-1]:
                stack.pop()
        
        # print(small_idx, stack)
        if small_idx == -1:
            return num
        num_list[small_idx], num_list[stack[-1]] = num_list[stack[-1]], num_list[small_idx]
        return int(''.join(num_list))


