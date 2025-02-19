# Problem: Product of the Last K Numbers - https://leetcode.com/problems/product-of-the-last-k-numbers/description/

class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.zeros = []

    def add(self, num: int) -> None:
        if num == 0:
            self.zeros.append(len(self.nums))
            num = 1
        
        if len(self.nums) != 0: self.nums.append(self.nums[-1] * num)
        else: self.nums.append(num)

    def getProduct(self, k: int) -> int:
        n = len(self.nums)
        lastZero = self.zeros[-1] if len(self.zeros) else -1
        if n - k <= lastZero <= n - 1:
            return 0
        elif len(self.nums) == k:
            return self.nums[-1]
        else:
            return self.nums[n - 1] // self.nums[n - k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)