class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # try:
        #     if haystack.index(needle):
        #         return needle.index()
        #     else:
        #         return -1
        # except ValueError:
        #     return -1
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
print(Solution().strStr("leetcode","leeto"))