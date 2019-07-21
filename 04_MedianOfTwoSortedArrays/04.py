class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
            :type nums1: List[int]
            :type nums2: List[int]
            :rtype: float
            """
        lenA = len(nums1); lenB = len(nums2)
        if (lenA + lenB) % 2 == 1:
            return self.findKth(nums1, nums2, (lenA + lenB)/2 + 1)
        else:
            return (self.findKth(nums1, nums2, (lenA + lenB)/2) + self.findKth(nums1, nums2, (lenA + lenB)/2 + 1)) * 0.5



def findKth(self, nums1, nums2, k):
    if len(nums1) == 0:
        return nums2[k-1]
        if len(nums2) == 0:
            return nums1[k-1]
    if len(nums2) > len(nums1):
        return self.findKth(nums2,nums1,k)
        if k == 1:
            return min(nums1[0],nums2[0])
    p = min(k / 2, len(nums2))
        if nums1[p-1] < nums2[p-1]:
            return self.findKth(nums1[p:],nums2,k-p)
else:
    return self.findKth(nums1,nums2[p:],k-p)


