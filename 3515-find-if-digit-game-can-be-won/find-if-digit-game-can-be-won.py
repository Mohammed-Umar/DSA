class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single_digit_nums = []
        double_digit_nums = []

        for num in nums:
            if num < 10:
                single_digit_nums.append(num)
            else:
                double_digit_nums.append(num)
               
        return sum(single_digit_nums) > sum(double_digit_nums) or sum(single_digit_nums) < sum(double_digit_nums)