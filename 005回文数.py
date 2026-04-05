class Solution:
    def longestPalindrome(self, s: str) -> str:
        #这个题是字符串的
        def expand(left,right):
            while(left>=0 and right<len(s) and s[left]==s[right]):
                left=left-1
                right=right+1

            return s[left+1:right]

        res=""
#回文数长度的奇偶
        for i in range(len(s)):
            s1=expand(i,i)
            s2=expand(i,i+1)
            res=max(res,s1,s2,key=len)

        return res
