class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        flag = 0
        for i in range(32):
            if n == pow(4,i):
                return True
        else:
            return False