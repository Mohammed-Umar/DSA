class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []
# first insert the numbers in the separate arrays.
        for num in nums:
            if nums.index(num) == 0:
             arr1.append(num)
            elif nums.index(num) == 1:
                arr2.append(num)

        for i in range(2,len(nums)):
            if arr1[-1] > arr2[-1]:
                  arr1.append(nums[i])
            elif arr2[-1] > arr1[-1]:
                  arr2.append(nums[i])

#After insertion append or merge the arrays 
        return arr1 + arr2