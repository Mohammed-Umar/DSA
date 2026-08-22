class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l_s1 = len(word1)
        l_s2 = len(word2)
        diff_l = abs(l_s2 - l_s1)
        result = ""

        if l_s1 == l_s2:
            for i in range(l_s1):
                result += word1[i] + word2[i]
        elif l_s2 > l_s1:
            for i in range(l_s1):
                result += word1[i] + word2[i]
            result += word2[l_s1:]
        else:
            for i in range(l_s2):
                result += word1[i] + word2[i]
            result += word1[l_s2:]
        return result
