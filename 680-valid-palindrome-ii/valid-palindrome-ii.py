class Solution:
    def validPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1

        while left < right:

            if s[left] != s[right]:

                changed_s1 = s[:left] + s[left + 1:]
                changed_s2 = s[:right] + s[right + 1:]

                # Check changed_s1
                left_new = 0
                right_new = len(changed_s1) - 1
                flag1 = 1

                while left_new < right_new:
                    if changed_s1[left_new] != changed_s1[right_new]:
                        flag1 = 0
                        break

                    left_new += 1
                    right_new -= 1

                # Check changed_s2
                left_new2 = 0
                right_new2 = len(changed_s2) - 1
                flag2 = 1

                while left_new2 < right_new2:
                    if changed_s2[left_new2] != changed_s2[right_new2]:
                        flag2 = 0
                        break

                    left_new2 += 1
                    right_new2 -= 1

                return bool(flag1 or flag2)

            left += 1
            right -= 1

        return True