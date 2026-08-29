class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a = None
        b = None

        nums = list(range(1, n))

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                add_up = nums[i] + nums[j]

                if add_up == n:
                    if '0' not in str(nums[i]) and '0' not in str(nums[j]):
                        a = nums[i]
                        b = nums[j]
                        return [a, b]

        return [a, b]
