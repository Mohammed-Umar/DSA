class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        result = []
        for item in nums:
            result.append(item ** 2)
        result.sort()
        return result