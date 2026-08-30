class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        min_loc = nums.index(min(nums))
        max_loc = nums.index(max(nums))

        left = min(min_loc,max_loc)
        right = max(min_loc,max_loc)

        delete_left = right + 1
        delete_right = n - left
        delete_both_sides = (left + 1) + (n - right)

        return min(delete_left , delete_right , delete_both_sides)
