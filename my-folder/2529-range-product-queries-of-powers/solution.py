class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        # powers composed of min num of powers of 2 that sum to n
        # increasing order

        # queries[i] = [left_i, right_i]
        # 1 query: find product of all powers[j] left_i <= j <= right_i

        # return array answers, equal in length to queries 
        # answers[i] = answer to ith query

        # calculate powers
        # answer queries -> product of nums within query index

        powers = []
        sum_powers = 0
        i = 0

        # how do we calculate min num of powers without greedy
        # powers can repeat

        # why would greedy not work?
        # n = 53
        # greedy = [1, 2, 4, 8, 16, 32] => 63
        # [1,2,]

        while sum_powers < n:
            powers.append(2**i)
            sum_powers += 2**i
            i += 1
        # 8 + 2 = 10
        # max val i.e., < sum_powers - n
        def get_max_val(target):
            val = 0
            for i in range(len(powers)):
                if powers[i] < target:
                    val = max(val, powers[i])
                else:
                    break
            return val
        while sum_powers > n:
            if sum_powers - n in powers:
                powers.remove(sum_powers - n)
                sum_powers = n
            else:
                val = get_max_val(sum_powers - n)
                sum_powers = sum_powers - val
                powers.remove(val)

        print(powers, len(powers))
        ans = []
        prefix_multiplier = [1]
        for i in range(len(powers)):
            prefix_multiplier.append(
                prefix_multiplier[-1] * powers[i]
            )
        prefix_multiplier = prefix_multiplier[1:]
        print('prefix_multiplier', prefix_multiplier)
        for q in queries: 
            st, ed = q[0], q[1]
            if st == ed:
                ans.append(powers[ed] % (10 ** 9 + 7))
            elif st == 0:
                ans.append(prefix_multiplier[ed] % (10 ** 9 + 7))
            else:
                
                ans.append(prefix_multiplier[ed]// prefix_multiplier[st-1] % (10 ** 9 + 7))

        return ans

        # prefix multiply
        # 2,4,8,10
        # 2,8,64,640
        # 
