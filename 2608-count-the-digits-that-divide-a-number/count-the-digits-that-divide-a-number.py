class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        num_copy = num
        while num > 0:
            digit = num % 10
            num = num // 10
            if num_copy % digit == 0:
                count += 1
        return count 