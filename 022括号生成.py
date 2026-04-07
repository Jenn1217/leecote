# 回溯，dfs相当于构造一棵树，但是它很慢
# 在

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]

        def dfs(path, left,right):
            #数字 n 代表生成括号的对数
            if len(path)==n*2:
                return res.append(path)

            if left < n:
                dfs(path+'(',left+1,right)

            if right<left:
                dfs(path+')',left,right+1)
# 在这里一直报错你懂吗？path是会一直更新的但是res仅仅是保存结果的情况。
        dfs("",0,0)

        return res
