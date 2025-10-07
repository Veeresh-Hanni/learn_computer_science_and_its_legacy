from typing import List


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # Pointers for the last valid elements in nums1 and nums2
        nums1_index = m - 1
        nums2_index = n - 1
        # Pointer for the last position in nums1
        merge_index = m + n - 1

        # Merge nums2 into nums1 starting from the end
        while nums2_index >= 0:
            if nums1_index >= 0 and nums1[nums1_index] > nums2[nums2_index]:
                nums1[merge_index] = nums1[nums1_index]
                nums1_index -= 1
            else:
                nums1[merge_index] = nums2[nums2_index]
                nums2_index -= 1
            merge_index -= 1

        print(nums1)

result = Solution()

result.merge([1,2,3,0,0,0],3,[2,5,6],3)