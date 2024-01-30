class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        margenum = []
        m, n = len(nums1), len(nums2)
        seen1, seen2 = 0, 0

        while seen1 < m and seen2 < n:
            if nums1[seen1] < nums2[seen2]:
                margenum.append(nums1[seen1])
                seen1 += 1
            else:
                margenum.append(nums2[seen2])
                seen2 += 1

        while seen1 < m:
            margenum.append(nums1[seen1])
            seen1 += 1

        while seen2 < n:
            margenum.append(nums2[seen2])
            seen2 += 1

        total_elements = m + n
        if total_elements % 2 == 0:
            median = (margenum[total_elements // 2 - 1] + margenum[total_elements // 2]) / 2
        else:
            median = margenum[total_elements // 2]

        return median
