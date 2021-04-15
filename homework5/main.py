from stack import Stack

stack = Stack()
print(stack.elements)
print(stack.is_empty())



stack.push(1)
print(stack.elements)
print(stack.is_empty())

stack.push(5)
print(stack.elements)

stack.push(3)
print(stack.elements)

stack.push(8)
print(stack.elements)

stack.remove()
print(stack.elements)

calced_stack = calc(my_stack)
for i in calced_stack:
	print(i)



