#重点在意之挪动一方
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1

        maxa=0
        while(left<right):
            area=(right-left)*min(height[left],height[right])

            maxa=max(area,maxa)

            if(height[left]<height[right]):
                left=left+1
            else:
                right=right-1

        return maxa
