from typing import List


def removeDuplicates( nums: List[int]) -> int:
        dubs = {}

        for num in nums:
            if num not in dubs:
                dubs[num] = 1
            else:
                dubs[num] += 1
                
        unique = [k for k in dubs if dubs[k] <= 1]
        return int(unique)

print(removeDuplicates([1,1,2]))