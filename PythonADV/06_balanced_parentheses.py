from collections import deque

input_string = input()
our_stack = deque()
valid_pairs = {
    ")": "(",
    "}": "{",
    "]": "["
}

from_stack = ""
balanced = True

for each in input_string:
    if each in "({[":
        our_stack.append(each)
    else:
        if not our_stack:
            balanced = False
            break
        else:
            from_stack = our_stack.pop()
        from_dict = valid_pairs[each]
        if from_stack != from_dict:
            balanced = False
            break

if balanced and len(our_stack) == 0:
    print("YES")
else:
    print("NO")
