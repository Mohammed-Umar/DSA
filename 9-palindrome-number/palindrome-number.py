class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        copy_str = ""
        for digit in x_str:
            if not digit.isnumeric():
                return False

            else:
                copy_str += digit

        if copy_str == x_str[::-1]:
            return True
        else:
            return False