class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            return self.findMedianSortedArrays(nums2, nums1)
        half = (len(nums1) + len(nums2)) // 2
        l, r = -1, len(nums1)
        while l <= r:
            mid1 = (r - l) // 2 + l
            l1 = float('-inf') if mid1 < 0 else nums1[mid1]
            r1 = float('inf') if mid1 + 1 >= len(nums1) else nums1[mid1 + 1]
            mid2 = half - mid1 - 2
            l2 = float('-inf') if mid2 < 0 else nums2[mid2]
            r2 = float('inf') if mid2 + 1 >= len(nums2) else nums2[mid2 + 1]

            if l1 <= r2 and l2 <= r1:
                break
            elif l1 > r2:
                r = mid1 - 1
            else:
                l = mid1 + 1
        print(l1, r1, l2, r2)
        if (len(nums1) + len(nums2)) % 2 == 1:
            return min(r1, r2)
        else:
            return (max(l1, l2) + min(r1, r2)) / 2
