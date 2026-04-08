# 类里的方法调用必须带self
# 双向链表里是Node结构用于知道谁先用谁后用
# cache相当于指针，存的是Node对象的引用


class Node:
    def __init__(self,key=0,value=0):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None 

class LRUCache:
    #哈希表 + 双向链表

    def __init__(self, capacity: int):
        self.capacity=capacity
        # 负责 O(1) 找到某个 key 对应的节点。
        self.cache={}
        # 双向链表用来维护节点的最近使用顺序。
        #self.head=Node()
        #self.tail=Node()
        self.head = Node()
        self.tail = Node()

        self.head.next=self.tail
        self.tail.prev=self.head

    # 必掌握的函数操作
    # 删除节点node
    def _remove(self,node:Node)->None:
        prev=node.prev
        nxt=node.next
        prev.next=nxt
        nxt.prev=prev
        # 用不用释放这个node节点的空间？

    def _add_to_head(self,node):
        #把节点插到头部，标志着这个节点被刚刚使用过
        #双向链表怎么知道谁是头谁是尾巴呢
        # self 代表这个对象自己，即 LRUCache
        # head <-> node <-> A <-> B <-> tail

        node.prev=self.head
        node.next=self.head.next
        self.head.next.prev=node 
        self.head.next=node


    def _move_to_head(self, node):
        # 不创建新的节点，就是移动
        #删掉原位置上的节点
        self._remove(node)
        #插到头部
        self._add_to_head(node)

    def _remove_tail(self)->Node:
        # head <-> node <-> A <-> B <-> tail
        # head <-> node <-> A <-> tail
        # 有了头尾节点就等于处理任何一个节点都可以当作一个普通节点去看
        node=self.tail.prev
        self._remove(node)
        return node        

    def get(self, key: int) -> int:
        # 如果找到节点，那就返回他的值。并且把它移动到头部
        if key not in self.cache:
            return -1
        
        node=self.cache[key]
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        # 1.key 已经存在，更新value，移到头部
        # 2. key不存在，
        # 创建新节点 放到头部 写入cache 超容量删除尾部节点，并且删除cache中的内容
        # 情况1 
        if key in self.cache:
            node=self.cache[key]
            node.value=value
            self._move_to_head(node)
        else:
            node=Node(key,value)
            self._add_to_head(node) 
            self._move_to_head(node)
            self.cache[key]=node

            if (len(self.cache)>self.capacity):
                removed=self._remove_tail()
                del self.cache[removed.key]



        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
