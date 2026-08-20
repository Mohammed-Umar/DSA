class Solution:
    def firstUniqChar(self, s: str) -> int:
        target_count = 1
        for letter in s:
            if s.count(letter) == target_count:
                return s.index(letter)
        else:
            return -1