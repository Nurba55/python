class Stack(object):
    def _init_(self):
        self.elements = []
        
    def push(self, element):
        self.elements.append(element)

    def is_empty(self):
        if not self.elements:
            return True
        else:
            return False
    
    def remove(self):
        is not self.is_empty():
            self.elements.pop()
    
    def calc(self):
        if len(self.elements) >=2:
            i=0:
            while i < len(self.elements) - 1:
                yield self.elements[i] * self.elements[i +1]
                i += 1
        else:
            return None

        pass
        


def push(stack,element):
    stack.append(element)
    return stack

def is_empty(stack):
    if not stack:
        return True
    else:
        return False

def remove(stack):
    if not is_empty(stack):
        stack.pop()
    return stack

def calc(stack):
    i = 0
    while i < len(stack) - 1:
        yield stack[i] * stack[i + 1]
        i += 1
    
        




	
