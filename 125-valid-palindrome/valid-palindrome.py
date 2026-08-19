class Solution:
    def isPalindrome(self, s: str) -> bool:
        c_str = ""
        for letter in s:
            if letter.isalnum():
                c_str += letter.lower()
        print(c_str)
        dup_str = c_str[::-1]

        if dup_str == c_str:
           return True
        else:
            return False
