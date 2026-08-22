class Solution:
    def checkDivisibility(self, n: int) -> bool:
        # sum of digits
        copy_n = n
        sum = 0
        prod = 1
        while n > 0:
            digit = n % 10
            sum = digit + sum
            prod = prod * digit
            n = int(n / 10)
        result = sum + prod
        return copy_n % result == 0
        
