class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            return self.findMedianSortedArrays(nums2, nums1)
        total_length = len(nums1) + len(nums2)
        half_length = total_length // 2
        l, r = 0, len(nums1) - 1
        while True:
            mid = (l + r) // 2
            other = half_length - mid - 2
            l1 = nums1[mid] if mid >= 0 else float('-inf')
            r1 = nums1[mid + 1] if mid + 1 < len(nums1) else float('inf')
            l2 = nums2[other] if other >= 0 else float('-inf')
            r2 = nums2[other + 1] if other + 1 < len(nums2) else float('inf')
            if l1 > r2:
                r = mid - 1
            elif l2 > r1:
                l = mid + 1
            elif total_length % 2 == 0:
                return (max(l1, l2) + min(r1, r2))/2
            else:
                return min(r1, r2)
