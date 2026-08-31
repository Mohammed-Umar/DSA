class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        copy_x = x
        sum_x = 0
        digit = 0
        while x > 0:
            digit = x % 10
            x //= 10
            sum_x = sum_x + digit

        return sum_x if copy_x % sum_x == 0 else -1