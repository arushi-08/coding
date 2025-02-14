class ProductOfNumbers:

    def __init__(self):
        # store suffixproduct
        self.product = 1
        self.prefix_product = []

    def add(self, num: int) -> None:
        if num != 0:
            self.product *= num
            self.prefix_product.append(self.product)
        else:
            self.product = 1
            self.prefix_product = []

    # 3,0,2,5,4
    # 3,0,0,0,0
    # 3,0,2,10,40
    def getProduct(self, k: int) -> int:
        # 5-3=2 | 0,1,2,3,4
        # print(self.product)
        n = len(self.prefix_product)
        if k == n:
            return self.prefix_product[-1]
        elif k > n:
            return 0

        return self.prefix_product[-1] // self.prefix_product[-1-k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

# ["ProductOfNumbers","add","add","add","getProduct","add","add","add","getProduct","getProduct","getProduct","add","add"]
# [[],[0],[0],[9],[3],[8],[3],[8],[5],[4],[6],[8],[8]]

# [0,0,9, getProduct, 8,3,8, getProduct, getProduct, getProduct,8,8]
# getProduct(3)
# getProduct(5)
# getProduct(4)
# getProduct(6)

# 

