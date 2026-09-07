class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ = sum(nums[:k])
        max_value = summ
        for i in range(k,len(nums)):
            summ = summ + nums[i] - nums[i-k]
            max_value = max(max_value,summ)
        return max_value/k