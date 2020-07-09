class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.mono_q = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        index = len(self.mono_q)-1 if len(self.mono_q) else -1
        while index>=0 and self.mono_q[index]>x:
            index-=1
        self.mono_q.insert(index+1,x)
        
        

    def pop(self) -> None:
        n = self.stack.pop()
        for i in range(len(self.mono_q)):
            if self.mono_q[i]==n:
                self.mono_q.pop(i)
                break
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mono_q[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()