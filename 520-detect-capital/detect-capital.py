class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        word_len = len(word)
        upper_count = 0
        lower_count = 0

        for letter in word:
            if letter.isupper():
                upper_count += 1
            elif letter.islower():
                lower_count += 1

        # Only first letter is capitalized
        if word[0].isupper() and lower_count == word_len - 1:
            return True

        # All uppercase or all lowercase
        elif lower_count == word_len or upper_count == word_len:
            return True

        # Invalid case
        else:
            return False