class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        # Sort the array first
        nums.sort()
        arr = []
        i = 0
        j = 1
        while i < len(nums) and j < len(nums):
            arr.append(nums[j])
            arr.append(nums[i])
            i += 2
            j += 2
        return arr
