class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length=len(digits)

        for i in range(length-1,-1,-1):
            if digits[i]<9:
                digits[i] += 1
                return digits          # 不再进位，直接结束
            digits[i] = 0

        return [1]+digits

#遗忘点：
#这个题体现了range的用法

#理解题意很重要，或许你不必搞这么麻烦  
