class Solution:
    #字典的用途，标准对照
    #enumerate 的用法， 返回序列和序列所对应的内容
    #超过字典、str本身长度
    #str的遍历 从左往右 1->len(s)-1
    def romanToInt(self, s: str) -> int:
         # 1. 创建一个哈希表（字典）来存储罗马数字的数值
        roman_map={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        total=0
        #从左往右
        for i, charnum in enumerate(s):
            current_n=roman_map[s[i]]
            
            if i<len(s)-1 and current_n<roman_map[s[i+1]]:
                total-=current_n
            else:
                total+=current_n

        return total

 
