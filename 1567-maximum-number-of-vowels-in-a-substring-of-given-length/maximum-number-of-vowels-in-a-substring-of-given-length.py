class Solution:

  def maxVowels(self, s: str, k: int) -> int:
    vowels = set("aeiou")

    # Count vowels in the first window of size k
    current_count = sum(1 for i in range(k) if s[i] in vowels)
    max_count = current_count

    # Slide the window across the rest of the string
    for i in range(k, len(s)):
      # Add the incoming character
      if s[i] in vowels:
        current_count += 1
      # Remove the outgoing character
      if s[i - k] in vowels:
        current_count -= 1

      max_count = max(max_count, current_count)

    return max_count