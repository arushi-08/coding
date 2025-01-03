class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # smallest int w same digits and greater in value than n
        # next greater element
        # 123 -> 132
        # 213 -> 231
        # 132 -> 213
        
        # find 1st idx, where i < i+1,
        # if not exists - return -1 e.g 4321
        # if found - (4123), find the next greater elem in range (i+1:), swap i with nge
        # sort arr[i+1:]
        # return arr[:i] + sorted(arr[i+1:])
        
        # 241 - 412 | 2415 - 4125 - find next greater elem, and 

        n_str = list(str(n))
        n_sorted_list = sorted(n_str)
        if ''.join(n_sorted_list[::-1]) == n_str:
            return -1

        ans = ''
        smaller_idx = len(n_str)-1

        for i in range(len(n_str)-2,-1,-1):
            if n_str[i] < n_str[i+1]:
                smaller_elem = 'inf'
                for j in range(i+1,len(n_str)):
                    if smaller_elem > n_str[j] and n_str[j] > n_str[i]:
                        smaller_idx = j
                        smaller_elem = n_str[j]

                n_str[i], n_str[smaller_idx] = n_str[smaller_idx], n_str[i]
                res = ''.join(n_str[:i+1] + sorted(n_str[i+1:]))
                if int(res) > 2**31 - 1:
                    return -1
                return int(res)
                
        return -1


        
