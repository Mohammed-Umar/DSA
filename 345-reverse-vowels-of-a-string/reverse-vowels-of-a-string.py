class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        stack = []
        s_list = list(s)

        # Step 1: Collect vowels and place placeholders
        for i in range(len(s_list)):
            if s_list[i] in vowels:
                stack.append(s_list[i])
                s_list[i] = "_"

        # Step 2: Replace placeholders with vowels from the stack (LIFO order)
        for i in range(len(s_list)):
            if s_list[i] == "_":
                s_list[i] = stack.pop()

        return "".join(s_list)