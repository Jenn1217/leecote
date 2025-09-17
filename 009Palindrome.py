class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 :
            return False
        #类型转换错误，只有str
        s1=str(x)
        #字符串不能直接反转,将字符串转换成list，之后将list反转
        #那为什么s2（字符串）== s1（list）两个类型不同还可以进行比较？
        s2=s1[::-1]
        return s1==s2

