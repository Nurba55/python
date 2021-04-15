from stack import *

my_stack = create_stack()
print(my_stack)

print(is_empty(my_stack))

push(my_stack,1)
print(my_stack)
print(is_empty(my_stack))

push(my_stack, 5)
print(my_stack)

push(my_stack, 3)
print(my_stack)

push(my_stack, 8)
print(my_stack)

remove(my_stack)
print(my_stack)

calced_stack = calc(my_stack)
for i in calced_stack:
	print(i)



