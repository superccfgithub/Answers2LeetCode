#question name:Min Stack
#question link:https://leetcode.com/problems/min-stack/
#Runtime: 112 ms

#-------------------Submitted Code-------------------------
class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self.s = [] #this stack is the full stack
        self.mins = []#this stack maintains the minvalue stack
    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.s.append(x)
        if not self.mins:
            self.mins.append(x)
        elif x <= min(self.mins):
            self.mins.append(x)
            
    # @return nothing
    def pop(self):
        if not self.s:
            return
        stop = self.s[len(self.s)-1]
        minstop = self.mins[len(self.mins)-1]
        if stop == minstop:
            self.mins.pop() 
        self.s.pop()

    # @return an integer
    def top(self):
        if not self.s:
            return 0
        return self.s[len(self.s)-1]

    # @return an integer
    def getMin(self):
        if not self.mins:
            return 0
        return self.mins[len(self.mins)-1]