def arrayConcat(nums1: list[int], nums2: list[int]) -> list[int]:
    arr = []
    n = max(len(nums1), len(nums2))
    for i in range(max):
        if nums1[i] < nums2[i]:
            arr.append(nums1[i])
        else:
            arr.append(nums2[i])


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pass