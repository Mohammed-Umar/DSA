class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = len(strs[0])
        for word in strs:
            if len(word) < min_len:
                min_len = len(word)

        reached_idx = -1
    
        # Check prefixes of length 1, 2, 3...
        for i in range(1, min_len + 1):

            prefix = strs[0][0:i]

            # Check if every word has the same prefix
            if all(word[0:i] == prefix for word in strs):
                reached_idx = i
            else:
                break

        if reached_idx != -1:
            return strs[0][0:reached_idx]
        else:
            return ""