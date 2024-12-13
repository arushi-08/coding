class Solution:
    def smallestNumber(self, pattern: str) -> str:
        
        # given 0 indexed string
        # and pattern
        # return smallest possibile string following the pattern

        # IIIDIDDD
        # 1

        # DDDI
        # 3214

        # if we see D, count how many d's are there
        # if we see i, keep doing normal j

        # if we see i+1 == D
        # we need to put bigger number followed by smaller number
        # so the smaller number has to be bigger than previous last num added to ans


        
        ans = ''
        d_count = 0
        i_count = 0
        max_num = 0

        for i in range(-1, len(pattern)-1):
            if pattern[i+1] == 'I':
                max_num = max(max_num, i_count)
                if d_count:
                    max_num += d_count + 1
                    i_count = max_num - d_count
                    val = max_num
                    while d_count:
                        ans += str(val)
                        val -= 1
                        d_count -= 1
                else:
                    i_count = max(max_num, i_count) + 1
                # print('i_count', i_count)
                ans += str(i_count)
                max_num = max(max_num, i_count)
            else:
                d_count += 1
            
        # problem is the i_count is not tracking what numbers are already done in ans
        
        if pattern[-1] == 'I':
            i_count = max(max_num, i_count) + 1
            ans += str(i_count)
        else:
            # print('max_num', max_num, 'i_count', i_count, 'd_count', d_count)
            max_num += d_count + 1
            val = max_num
            while d_count + 1:
                ans += str(val)
                val -= 1
                d_count -= 1

        return ans
