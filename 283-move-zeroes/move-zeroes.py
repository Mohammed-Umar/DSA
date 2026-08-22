class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        result = []

        for num in nums:
            if num != 0:
                result.append(num)

        zero_count = len(nums) - len(result)

        for i in range(zero_count):
            result.append(0)

        nums[:] = result