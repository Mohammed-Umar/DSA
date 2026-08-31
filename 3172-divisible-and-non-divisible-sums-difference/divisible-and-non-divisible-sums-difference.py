class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        nums = list(range(1,n+1))
        divisible = list()
        non_divisible = list()
        for num in nums:
            if num % m == 0:
                divisible.append(num)
            else:
                non_divisible.append(num)
        sum1 = sum(non_divisible)
        sum2 = sum(divisible)

        return sum1 - sum2

        