class Solution:

  def uniqueOccurrences(self, arr: List[int]) -> bool:
    count_stack = []

    # Iterate through unique elements only
    for item in set(arr):
      count = arr.count(item)
      if count not in count_stack:
        count_stack.append(count)
      else:
        return False

    return True