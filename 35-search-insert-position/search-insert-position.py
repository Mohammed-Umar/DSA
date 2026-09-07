class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        for num in nums:
            if target < num:
                return nums.index(num)
        return len(nums)