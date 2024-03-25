# from collections import Trie
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        # lexicographically sorting products
        products = sorted(products)
        # --no use tries to store the characters 
        # simple string start
        output = []
        for i in range(len(searchWord)):
            recommendations = []
            for prod in products:
                if prod[:i+1] == searchWord[:i+1]:
                    recommendations.append(prod)
                if len(recommendations) == 3:
                    break
            
            output.append(recommendations)
    
        return output


