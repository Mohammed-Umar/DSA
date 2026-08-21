class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result_num = []
        result = []
        maxCandies = max(candies)

        for i in range(len(candies)):
            result_num.append(candies[i] + extraCandies)

        for x in result_num:
            if x >= maxCandies:
                result.append(bool(1))
            else:
                result.append(bool(0))
            
        return result

        