 class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 遇到非0就往前挪动
        i=0
        for j in range(len(nums)):
            if nums[j]!=0:
                nums[j],nums[i]=nums[i],nums[j]
                i+=1
                
