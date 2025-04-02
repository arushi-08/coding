class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        
        # given a string s of even length consisting of digits from 0 to 9
        # and 2 integers a and b
        # we can apply either of the following 2 ops:
        # add a to all odd indices, if digit becomes > 9, then take mod 14 % 10
        # rotate s to right by b positions, s = '3456', b=1, s becomes 6345

        # return lexicographically smallest string i can obtain by applying these ops

        # make s into min_s

        # s = 5525, a=9, b=2
        # 

        # if adding a doesn't decrease any of the odd index, then don't do it
        # rotate and bring the smallest element to front
        # either biggest to front -> apply a -> see if it becomes smallest element
        # else bring smallest to front

        # check if adding a to all odd idx, if any becomes lesser than smaller digit
        # for loop on s
        # convert a's odd idx to + a till the value becomes smaller
        # when it does
        # at the same time, see if rotating s is helping

        # either the max character converted to smaller < existing smaller
        # else opposite

        # current flaw: not doing op a number of times, till you get the same max_char?
        # 5+9 = 4 + 9 = 
        # 5+1+1+1+1+1+1+1+1
        # flaw 2: rotate s b num of positions
        

        # bfs
        # exhaustive search

        queue = deque()
        queue.append(s)
        min_s = s
        visited = set()
        visited.add(s)

        while queue:
            curr_s = queue.popleft()
            min_s = min(min_s, curr_s)
            # either add a at odd pos
            curr_s_list = list(curr_s)
            for i in range(1, len(curr_s), 2):
                curr_s_list[i] = str( (int(curr_s[i]) + a) % 10 )
            
            add_s_a = ''.join(curr_s_list)
            # other option b, rotate it
            rotate_s_b = curr_s[-b:] + curr_s[:-b]

            for new_s in [add_s_a, rotate_s_b]:
                if new_s not in visited:
                    queue.append(new_s)
                    visited.add(new_s)
        return min_s


