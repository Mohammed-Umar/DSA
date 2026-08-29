class Solution:
    def alternateDigitSum(self, n: int) -> int:
        count = 0
        sum_digits = 0
        while n > 0:
            digit = n % 10
            n //= 10
            if count % 2 == 0:
                sum_digits += digit
                
            else:
                sum_digits -= digit
            count += 1

        if count % 2 == 0:
            sum_digits = -sum_digits

        return sum_digits

