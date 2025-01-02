class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        ans = []
        for ast in asteroids:
            if ast < 0:
                destroyed = False
                while ans and ans[-1] > 0:
                    if ans[-1] < -ast:
                        ans.pop()
                        continue
                    if ans[-1] == -ast:
                        ans.pop()
                    destroyed = True
                    break
                if not destroyed:
                    ans.append(ast)
            else:
                ans.append(ast)
            
        return ans
        
            



