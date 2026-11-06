class Solution {
    public int majorityElement(int[] nums) {
      int n = nums.length;
      int cnt = 0;
      int ele = -1;

      for(int i = 0; i < n;i++) {
        if(cnt == 0) {
            ele = nums[i];
            cnt+=1;
        }
        else if(nums[i] == ele) {
            cnt+=1;
        }
        else{
            cnt-=1;
        }
      }

      int cnt1 = 0;
      for(int i = 0;i < n;i++) {
        if(nums[i] == ele){
            cnt1+= 1;
        }
      } 
      if(cnt1 >= n/2) return ele;
      return -1;
    }
}