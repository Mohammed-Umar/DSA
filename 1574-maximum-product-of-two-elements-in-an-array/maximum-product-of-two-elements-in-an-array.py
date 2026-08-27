class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Sort the array
        nums.sort()
        result = (nums[-1] - 1) * (nums[-2] - 1)
        return result