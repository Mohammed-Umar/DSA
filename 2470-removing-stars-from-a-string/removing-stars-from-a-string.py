class Solution:
    def removeStars(self, s: str) -> str:
        stack_s = []
        for char in s:
            if char == '*':
                stack_s.pop()
            else:
                stack_s.append(char)
        return "".join(stack_s)