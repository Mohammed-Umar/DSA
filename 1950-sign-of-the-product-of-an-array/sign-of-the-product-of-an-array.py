class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prod = 1
        for num in nums:
            prod *= num
        return self.signFunc(prod)

    def signFunc(self,x):
        if x > 0:
            return 1
        elif x < 0:
            return -1
        elif x == 0:
            return 0