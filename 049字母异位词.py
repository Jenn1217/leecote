#重点是学到了defaultdict的这个数据结构
#它的组成结构就是{1:[1,2,3],2:[2,3,4]}
# 还有ord，转换字符为askii码
# tuple数据类型，只要确定了就不会改变，可以作为字典的key，但是list可以修改不能作为字典的key
# 把字母转化成为字母表的思维
# 最后一点转化为list

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        #这个东西是(a:[1,2,3])

        for ss in strs:
            count=[0]*26
            for c in ss:
                count[ord(c)-ord('a')]+=1

            key=tuple(count)
            d[key].append(ss)

        return list(d.values())
