# 重复如何除去，1 i重复 2. left和right重复
# 将三元变成两元
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        l1=[]
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            sum2=-nums[i]
            left=i+1
            right=len(nums)-1
            

            while(left<right):
                if nums[left]+nums[right]==sum2:
                    l1.append([nums[i],nums[left],nums[right]])
                    while(left<right and nums[left]==nums[left+1]):
                        left=left+1
                    while (left<right and nums[right]==nums[right-1]):
                        right=right-1
        
                    left=left+1
                    right=right-1
                elif nums[left]+nums[right]>sum2:
                    right=right-1
                else:
                    left=left+1

        return l1

