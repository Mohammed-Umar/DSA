class Solution:
    def reverseWords(self, s: str) -> str:
        list_words = s.strip().split(' ')
        result = ''
        for word in list_words:
            result += word[::-1] + ' '

        return result.strip()