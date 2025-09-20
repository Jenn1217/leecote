class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #重要的是怎样利用python 的特性
        #好喜欢cs

        #先判断是否为空
        if not nums:
            return 0

        n=len(nums)
        #slow代表不相同的数字个数
        #fast代表实际走的长度
        fast=slow=1

        while fast<n:
            if nums[fast]==nums[fast-1]:
                #前后两个数字相同的时候，slow不懂
                fast=fast+1
            else:
                #前后不同
                nums[slow]=nums[fast]
                slow=slow+1
                fast=fast+1

        return slow


