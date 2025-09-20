# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #这不是普遍的类型！！！
        empty=ListNode()
        #代表一个指针，用来记录当前连接到哪一部分了
        current=empty
        while list1 and list2:
            if list1.val<list2.val:
                current.next=list1
                list1=list1.next
            else:
                current.next=list2
                list2=list2.next                
            current=current.next
        if list1:
            current.next=list1
        elif list2:
            current.next=list2

        return empty.next
        
