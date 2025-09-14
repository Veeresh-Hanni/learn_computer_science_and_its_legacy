def longestCommonPrefix(strs: list[str]) -> str:
    sort = sorted(strs)
    first = sort[0]
    last = sort[::-1]
    for char in zip(strs):
        pass
strings = ["flower","flow","flight"]
print(longestCommonPrefix(strings))