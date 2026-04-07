class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 这个和其他数据的最大的不同就是，defaultdict在创建的时候必须在括号里标注value的类型，如果没有这个key，default会直接创建一个新的节点
        # 但是dict就会报错
        # set只适合查找在不在，不适合计数
        
        #这道题要理解子数组的意思，和前缀和的理解
        
        count=defaultdict(int)
        count[0]=1

        # 前缀和为pre
        pre=0
        # 出现了多少次,目前一共找到多少个和为 k 的子数组
        res=0

        for num in nums:
            pre+=num
            
            # pre-k 就是前面的子数组
            if pre - k in count:
                res += count[pre - k]

            count[pre]+=1

        return res 
            
