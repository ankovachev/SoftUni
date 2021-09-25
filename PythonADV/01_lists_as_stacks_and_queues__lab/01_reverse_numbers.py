from collections import deque

our_stack = deque()
current_input = input().split()
[our_stack.appendleft(each) for each in current_input]
print(' '.join(our_stack))
