#主要练习哈希表
import numpy as np
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #哈希表的解法，哈希表就是dict,在这里seek用于存储for循环已经便利过的词汇
        seek=dict()
        #key=num, value=i 因为dict查找key的速度快于value

        for i,num in enumerate(nums):
            if target-num in seek:
                #到底查找的是那一个数字，需要弄清楚
                return [seek[target-num],i]
            seek[num]=i
'''        
        numslen=len(nums)
        #np.array() 是用来转换现有数据的，而不是用来创建空数据结构的
        res=[]
        #range函数
        for i in range(numslen):
            for j in range(i+1,numslen):
                if nums[i]+nums[j]==target:
                    res.append(i)
                    res.append(j)
                    return res'''

