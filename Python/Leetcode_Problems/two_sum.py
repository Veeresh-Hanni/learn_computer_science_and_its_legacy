class Solution(object):
    def twoSum(self, nums: list, target: int) -> list:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index in range(len(nums)):
            for second_num in range(index + 1, len(nums)):
                if nums[index] + nums[second_num] == target:
                    return [index, second_num]


solution = Solution()
print(solution.twoSum([3, 2, 4], 6))
