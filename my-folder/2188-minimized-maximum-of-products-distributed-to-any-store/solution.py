class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        
        # given integer n, indicating there are n retail stores
        # m product types of varying amounts
        # quantities[i] = num of prods of type prod[i]
        # 
        # distribute all prods
        # 1 prod type but any amount
        # x - max num of products given to any store
        # min x

        # 11, 6
        # _,_,_,_,_,_
        # 3,3,3,3,3,3 = 3*6 = 18 > 17 -> can distribute
        
        # 1 to max(prod type) search range
        # FFFTTT
        # check if at most mid can be given to all stores
        def can_distribute(mid):
            # q is prod quant
            # mid is min possible num of quant distributed
            n_stores_till_now = 0
            for q in quantities:
                n_stores_till_now += math.ceil(q/mid)
            return n_stores_till_now <= n

        st = 1
        ed = max(quantities)
        res = ed
        while st <= ed:
            mid = (st + ed)//2
            if can_distribute(mid):
                res = mid
                ed = mid - 1
            else:
                st = mid + 1
        
        return res



