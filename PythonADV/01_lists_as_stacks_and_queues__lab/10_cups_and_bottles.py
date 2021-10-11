import sys
from collections import deque
from io import StringIO

input1 = """4 2 10 5
3 15 15 11 6
"""
input2 = """1 5 28 1 4
3 18 1 9 30 4 5
"""
input3 = """10 20 30 40 50
20 11
"""

sys.stdin = StringIO(input1)

cups = deque()
bottles = deque()
cups_input = input().split()
bottles_input = input().split()
is_filled_all_cups = False

[cups.append(int(each)) for each in cups_input]
[bottles.append(int(each)) for each in bottles_input]
current_wasted_water = 0
cuppernt_rest_water = 0
while True:

    current_bottle = bottles.pop()
    current_cup = cups[0]
    if current_bottle >= current_cup:
        cups.popleft()  # You can fill the cup
        current_wasted_water += current_bottle - current_cup
    else:
        current_rest_water = current_bottle - current_cup  # You can't fill the cup

    if not cups:
        is_filled_all_cups = True
        print(f"Bottles: {len(bottles_input)}")
        break
    if not bottles:
        print(f"Cups: {len(cups_input)}")
        break

# Converting all numbers to strings and print it
if is_filled_all_cups:
    [str(each) for each in bottles]
#    print(f"Bottles: {' '.join(bottles)}")  # Print all bottles split by space.
else:
    [str(each) for each in cups]
#    print(f"Cups: {' '.join(cups)}")  # Print all cups split by space.
# That's all, folks!
