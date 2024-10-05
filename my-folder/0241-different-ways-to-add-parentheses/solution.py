class Solution:
    operations = {
        '+': lambda x1, x2: (x1 + x2),
        '-': lambda x1, x2: (x1 - x2),
        '*': lambda x1, x2: (x1 * x2),
    }
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        res = []

        for i in range(len(expression)):
            char = expression[i]
            if char in self.operations:
                res1 = self.diffWaysToCompute(expression[:i])
                res2 = self.diffWaysToCompute(expression[i+1:])

                for r1 in res1:
                    for r2 in res2:
                        res.append(self.operations[char](r1, r2))
        
        if not res:
            return [int(expression)]

        return res
