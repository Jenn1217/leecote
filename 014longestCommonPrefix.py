import numpy as np

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #首先考虑特殊情况
        if not strs:
            return ""
        
        #纵向
        charlen, strslen=len(strs[0]),len(strs)

        #i代表最后公共前缀的长度
        #j代表1-strslen的strs序号
        for i in range(charlen):
            c=strs[0][i]
            #如果 长度 or 不相同
            if any( i==len(strs[j]) or c!=strs[j][i] for j in range(1,strslen)):
                return strs[0][:i]
