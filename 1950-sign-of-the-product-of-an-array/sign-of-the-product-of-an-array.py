class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prod = 1
        for num in nums:
            prod = prod * num
        
        return self.signFunc(prod)

    def signFunc(self,num):

        if num > 0:
            return 1

        elif num < 0:
            return -1
        
        else:
            return 0

