class Solution {
    public List<List<Integer>> threeSum(int[] nums) {

        Set<List<Integer>> resultSet = new HashSet<>();
        Arrays.sort(nums); // Sorting helps manage duplicates easily

        for (int i = 0; i < nums.length - 2; i++) {
            // Optimization: If the current number is positive, stop (can't sum to 0)
            if (nums[i] > 0) {
                break;
            }

            Set<Integer> seen = new HashSet<>();
            for (int j = i + 1; j < nums.length; j++) {
                int third = -(nums[i] + nums[j]);
                
                if (seen.contains(third)) {
                    List<Integer> triplet = Arrays.asList(nums[i], third, nums[j]);
                    resultSet.add(triplet); // HashSet automatically handles duplicate triplets
                }
                seen.add(nums[j]);
            }
        }

        return new ArrayList<>(resultSet);
    }
}  
    
