from sympy import true


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        mapping = {}
        used_chars = set()  # to track characters already mapped in t

        for cs, ct in zip(s, t):
            if cs in mapping:
                # If cs already mapped, it must map to the same ct
                if mapping[cs] != ct:
                    return False
            else:
                # If ct already used by another cs, not isomorphic
                if ct in used_chars:
                    return False
                mapping[cs] = ct
                used_chars.add(ct)

        return True
    
print(Solution().isIsomorphic("paper","title"))