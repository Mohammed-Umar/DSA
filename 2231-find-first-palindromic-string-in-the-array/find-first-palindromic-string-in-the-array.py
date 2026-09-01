class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            copy_word = word
            if copy_word == word[::-1]:
                return word
        return ""