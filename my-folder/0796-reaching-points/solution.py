class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        
        if sx > tx or sy > ty: return False

        
        # tx < ty
        while tx >= sx and ty >= sy:
            if sx == tx and sy == ty: return True

            if tx < ty:
                if tx > sx:
                    ty %= tx
                else:
                    return (ty-sy)%tx == 0 
            else:
                if ty > sx:
                    tx %= ty
                else:
                    return (tx-sx)%ty == 0
        
        return False
