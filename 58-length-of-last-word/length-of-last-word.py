class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        cln_s = s.strip()[::-1]

        for i in range(len(cln_s)):
            if cln_s[i].isspace():
                return i

        return len(cln_s)