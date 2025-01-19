class MinStack:

    def __init__(self):
        self.stack = []  # Main stack
        self.min_stack = []  # Temp stack to hold the min at each time at the top

        
    def push(self, val: int) -> None:
        self.stack.append(val)
                
        if self.min_stack:    
            # Compare the new value with the current minimum (top of min_stack)
            # Only add smaller or equal values to min_stack to keep the min value at the top
            if val <= self.min_stack[-1]:
                self.min_stack.append(val)
        else:
            # If min_stack is empty, push the first value to min_stack
            self.min_stack.append(val)

            
    def pop(self) -> None:
        # Remove the top value from the main stack
        del_val = self.stack.pop()
        # If the popped value is the minimum, delete it from min_stack
        if del_val == self.min_stack[-1]:
            self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()