class Solution {
    public void moveZeroes(int[] nums) {
        int zeroElementIndex = 0;
        for(int i = 0;i < nums.length;i++) {
            if(nums[i] != 0) {
                int temp = nums[zeroElementIndex];
                nums[zeroElementIndex] = nums[i];
                nums[i] = temp;
                zeroElementIndex++;
            }
        }
    }
}