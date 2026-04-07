# 本质上是斐波那契数列
# 使用两个数据去充当f(n-1) f(n-2)
# 不需要看前面走了多少，就看最后两部就可以
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n

        a=1  # 到第1阶的方法数
        b=2  # 到第2阶的方法数

        for i in range(3,n+1):
          # 右侧算完之后再算左侧的内容
          # 两者都向上走一步
          # 状态滚动更新
           a,b=b,b+a 

        return b
