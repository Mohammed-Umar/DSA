class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digit = 0
        sum_n = 0
        prod = 1
        while n > 0:
            digit = n % 10
            sum_n += digit
            prod *= digit
            n //=10
        return (prod - sum_n)