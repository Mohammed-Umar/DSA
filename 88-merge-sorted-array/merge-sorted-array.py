class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            nums1[m+i] = nums2[i]
        
        # sorting the num1 array
        # temp = 0
        # for i in range(len(nums1)-2):
        #     if nums1[i] > nums1[i+1]:
        #         temp = nums1[i]
        #         nums1[i] = nums1[i+1]
        #         nums1[i+1] = temp

        return nums1.sort()
        