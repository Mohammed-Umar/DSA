class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_digits = ""
        for digit in digits:
            str_digits += str(digit)
        n = int(str_digits) + 1
        digits = []
        while n > 0:
            digit = n % 10
            n //= 10
            digits.append(digit)
        digits.reverse()
        return digits
