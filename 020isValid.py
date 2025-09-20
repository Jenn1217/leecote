class Solution:
    def isValid(self, s: str) -> bool:
        #stack仅仅保存左括号
        
        if len(s)%2==1:
            return False
        
        #pairs使用右括号寻找左括号
        #在这里是一个字典，查东西很快
        pairs={
            ')':'(',
            ']':'[',
            '}':'{'
        }

#stack=[1,2,3,4]
#stack.pop()=4
#LIFO - Last In, First Out
        #利用pop将最后的元素
        stack=list()

        for ch in s:
            if ch in pairs:
              #重点是这里的逻辑，先判断ch是不是右括号，不是右括号就是左括号，左括号加入stack
              #stack的先进后出意味着，匹配一个走一个，【【【（（））】】】
                if not stack or stack[-1]!=pairs[ch]:
                    return False
                stack.pop()
                #无论是否匹配成功后都要将最后一个元素弹出
                #因为最后的返回机制就是判断stack是否为空，如果为空就证明所有匹配成功
            else:
                stack.append(ch) 

        return not stack
        
