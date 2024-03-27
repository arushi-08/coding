class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        # lexicographically sorting products
        products = sorted(products)
        # --no use tries to store the characters 
        # simple string start
        output = [[] for _ in searchWord]
        iproducts = products
        
        for i in range(len(searchWord)):
            for product in iproducts:
                if len(product) > i and product[i] == searchWord[i]:
                    output[i].append(product)
                elif len(output[i]) > 0:
                    break
            iproducts = output[i]
            output[i] = output[i][:3]
        
        return output
