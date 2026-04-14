import numpy as np

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 
        if not strs:
            return ""

        pex=strs[0]
        for s in strs[1:]:
            while not s.startswith(pex):
                pex=pex[:-1]
                if pex=="":
                    return ""

        return pex
