class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        keyChange = 0
        i = 0
        while i <= len(s) - 2:
            if s[i] != s[i+1]:
                keyChange += 1
            i += 1
        return keyChange

