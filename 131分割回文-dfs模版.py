def backtrack(参数, path):
    # 终止条件（收集答案）
    if 满足条件:
        res.append(path[:])
        return

    # 枚举所有选择
    for 选择 in 选择列表:
        
        if 不合法:
            continue

        # ① 做选择
        path.append(选择)

        # ② 递归
        backtrack(更新参数, path)

        # ③ 撤销选择（回溯）
        path.pop()

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # 回溯 =“我先试一下这个选择 → 不行我再撤回来”
        #选一段 → 判断回文 → 继续切 → 到底 → 存结果 → 回退 → 换一段
        def is_para(ss):
            return ss==ss[::-1]

        res=[]

        def dfs(start,path):
            # 如果已经到达最末尾的地方
            if start==len(s):
                res.append(path[:])
                return 

            # 枚举切的位置
            for end in range(start,len(s)):
                #这里为啥是end+1，因为一开始end=start，从start往后取
                #为啥还要取子串subs？
                #res用来存储结果
                #path代表试错路径？代表当前的内容
                #subs = s[start:end+1]
                subs=s[start:end+1]
                if is_para(subs):
                    path.append(subs)
                    #这里为啥是end+1不是start+1？
                    dfs(end+1,path)
                    path.pop()

        dfs(0,[])
        return res
