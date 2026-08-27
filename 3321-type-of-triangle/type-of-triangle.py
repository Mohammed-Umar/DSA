class Solution:
    def triangleType(self, nums: List[int]) -> str:
        flag = 0
        nums.sort()
        # check if it forms a triangle
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        if nums[0] + nums[1] > nums[-1]:
            flag = 1
        if flag:
            if nums[0] == nums[1] == nums[2]:
                return "equilateral"
            elif nums[0] != nums[1] != nums[2]:
                return "scalene"
            else:
                return "isosceles"

        else:
            return "none"
        