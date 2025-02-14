class ProductOfNumbers:

    def __init__(self):
        self.prefixProductArr = [1]
        self.maxZeroIndex = -1

    def add(self, num: int) -> None:
        if num == 0:
            self.maxZeroIndex = len(self.prefixProductArr)
        newAllProduct = self.prefixProductArr[-1] * num if num !=0 else 1
        self.prefixProductArr.append(newAllProduct)
       
        

    def getProduct(self, k: int) -> int:
        kIndex = len(self.prefixProductArr) - k
        if kIndex <= self.maxZeroIndex:
            return 0
        res = self.prefixProductArr[-1] // self.prefixProductArr[kIndex - 1]
        return int(res)
    

        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)