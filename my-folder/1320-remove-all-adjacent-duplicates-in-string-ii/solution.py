class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """store the count of consecutive same chars also in the stack"""
        stack = []
        group_count = 0
        for char in s:
            if stack and stack[-1][0] == char:
                group_count = stack[-1][1] + 1
                stack.append((char, group_count))
            else:
                stack.append((char, 1))
                group_count = 1

            if group_count == k:
                while stack and group_count:
                    stack.pop()
                    group_count -= 1

        return "".join([i[0] for i in stack])
            
            
