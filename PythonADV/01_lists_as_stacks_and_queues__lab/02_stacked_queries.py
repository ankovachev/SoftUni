from collections import deque

n = int(input())
our_stack = deque()
converted_list = []

for _ in range(n):
    query = input().split()
    command = query[0]

    if command == "1":
        current_value = int(query[1])
        our_stack.appendleft(current_value)
    elif command == "2":
        if our_stack:
            our_stack.popleft()
    elif command == "3":
        if our_stack:
            print(max(our_stack))
    elif command == "4":
        if our_stack:
            print(min(our_stack))

converted_list = [str(each) for each in our_stack]
print(", ".join(converted_list))
