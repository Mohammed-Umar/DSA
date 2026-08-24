class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
            arr_sum = sum(nums)
            digit_arr = []
            for item in nums:
                sum_n = 0
                digit = -1
                if item < 10:
                    digit = item
                    digit_arr.append(item)
                else:
                    
                    while item > 0:
                        digit = item % 10
                        sum_n = digit + sum_n
                        item = int(item / 10)
                    digit_arr.append(sum_n)
            print(digit_arr)
            return abs(arr_sum - sum(digit_arr))

            
                
                    