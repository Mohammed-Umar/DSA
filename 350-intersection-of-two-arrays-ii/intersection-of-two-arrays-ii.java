class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
     // 1. Sort both arrays first
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        
        List<Integer> result = new ArrayList<>();
        int i = 0, j = 0;
        
        // 2. Traverse both arrays using two pointers
        while (i < nums1.length && j < nums2.length) {
            if (nums1[i] < nums2[j]) {
                i++;
            } else if (nums1[i] > nums2[j]) {
                j++;
            } else {
                // Match found! Add to list only if it's unique (not a duplicate of the last added element)
                result.add(nums1[i]);
                i++;
                j++;
            }
        }
        
        // 3. Convert List to primitive int[] array
        int[] res = new int[result.size()];
        for (int k = 0; k < result.size(); k++) {
            res[k] = result.get(k);
        }
        
        return res;
    }
}   
    
