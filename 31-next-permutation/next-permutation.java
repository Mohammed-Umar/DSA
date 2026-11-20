class Solution {
    public void nextPermutation(int[] nums) {
        int n = nums.length;
        int idx = -1;

        // 1. Find the rightmost index where nums[i] < nums[i + 1]
        for (int i = n - 2; i >= 0; i--) {
            if (nums[i + 1] > nums[i]) {
                idx = i;
                break;
            }
        }

        // 2. If no such index exists, reverse the entire array
        if (idx == -1) {
            reverse(nums, 0, n - 1);
            return;
        }

        // 3. Find the rightmost element greater than nums[idx] and swap
        for (int i = n - 1; i > idx; i--) {
            if (nums[i] > nums[idx]) {
                int temp = nums[idx];
                nums[idx] = nums[i];
                nums[i] = temp;
                break;
            }
        }

        // 4. Reverse the suffix after idx to get the smallest lexicographical order
        reverse(nums, idx + 1, n - 1);
    }

    private void reverse(int[] nums, int left, int right) {
        while (left < right) {
            int temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;
            left++;
            right--;
        }
    }
}