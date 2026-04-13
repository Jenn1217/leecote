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


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #我建立一个哈希表，里面存的都是字符串前缀，
        #因为这一题求的是前缀之间的差，所以我需要不断的把前缀和加入进去
        #prefix[i] = prefix[j] - k
        #时间：O(n)
        #空间：O(n)
        #前缀和 → 出现次数
        indexmap={0:1}
        #当前走到的位置的前缀和
        cur_sum=0
        #最终答案：满足条件的子数组个数
        cnt=0

        for i in nums:
            cur_sum+=i

            if cur_sum-k in indexmap:
                #把“所有能和当前凑成 k 的历史前缀和个数”加到答案里
                cnt+=indexmap[cur_sum-k]

            indexmap[cur_sum]=indexmap.get(cur_sum,0)+1
        
        return cnt

            
