class Solution:
    def removeStars(self, s: str) -> str:
        stack_s = []

        for letter in s:
            if letter == "*":
                stack_s.pop()
            else:
                stack_s.append(letter)
        return "".join(stack_s)