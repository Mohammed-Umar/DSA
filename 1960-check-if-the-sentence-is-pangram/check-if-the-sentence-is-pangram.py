class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        chk_set = set(sentence)

        return len(chk_set) == 26