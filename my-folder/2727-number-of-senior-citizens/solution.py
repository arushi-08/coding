class Solution:
    def countSeniors(self, details: List[str]) -> int:
        
        n_seniors = 0
        for det in details:
            if int(det[11:13]) > 60:
                n_seniors += 1
        
        return n_seniors
