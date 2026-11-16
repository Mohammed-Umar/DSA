class Solution {
    public void sortColors(int[] nums) {
        int zeroc = 0;
        int onec = 0;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) zeroc++;
            else if (nums[i] == 1) onec++;
        }

        for (int i = 0; i < zeroc; i++) {
            nums[i] = 0;
        }
        // Run until zeroc + onec
        for (int i = zeroc; i < zeroc + onec; i++) {
            nums[i] = 1;
        }
        // Start from zeroc + onec
        for (int i = zeroc + onec; i < nums.length; i++) {
            nums[i] = 2;
        }
    }
}
