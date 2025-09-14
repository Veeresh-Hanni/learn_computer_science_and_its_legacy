class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # start = 0
        # end = len(nums) - 1


        # while start <= end:
        #     if (nums[start] == val and nums[end] == val):
        #         nums.remove(val)
        #         nums.remove(val)
        #     elif (nums[start] == val or nums[end] == val):
        #         nums.remove(val)
        #     start += 1
        #     end -= 1

        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
print(Solution().removeElement([3,3], 3))