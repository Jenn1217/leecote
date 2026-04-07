'''
这题我一开始会想到先排序再遍历，这样能做出来，但复杂度是 O(n log n)，不符合题目要求的 O(n)。
所以正确做法是用 哈希集合 set。

核心思想是：

只从连续序列的起点开始往后枚举。

具体来说：

先把所有数字放进 set，这样查找某个数在不在是 O(1)
遍历每个数 num
如果 num - 1 不在 set 里，说明它是一个连续序列的起点
然后不断检查 num + 1、num + 2 是否存在，统计这一段连续长度
更新最大值

为什么是 O(n)？

因为每个数最多只会被当作某个连续序列的一部分检查一次，不会反复重复扫描，所以总复杂度是 O(n)。'''


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        max_length=0

        for num in num_set:
            #如果num在 num_Set就不用管
            #num不在才开始数数
            if num-1 not in num_set:
                cur=num
                length=1

                while cur+1 in num_set:
                    length+=1
                    cur+=1

            max_length=max(length,max_length)

        return max_length
