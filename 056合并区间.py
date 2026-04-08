# lambda 的使用方式，他是一个匿名函数，lambda 输入变量: 返回值表达式
# 方位感很重要
# not res，当这个为空的时候res不能超过长度

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        #intervals.sort(key=lambda x: x[0])

        res=[]

        for interval in intervals:
            if not res or interval[0]>res[-1][1]:
                res.append(interval)
            else:
                res[-1][1]=max(interval[1],res[-1][1])

        return res
