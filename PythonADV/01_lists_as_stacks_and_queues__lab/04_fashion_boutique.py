import sys
from collections import deque
from io import StringIO

# input1 = """5 4 8 6 3 8 7 7 9
# 16
# """
# input2 = """1 7 8 2 5 4 7 8 9 6 3 2 5 4 6
# 20
# """
#
# sys.stdin = StringIO(input2)
clotes_in_box = deque()
boxes_input = input().split()
[clotes_in_box.append(int(each)) for each in boxes_input]
capacity = int(input())
number_of_racks = 1
current_piece = 0
current_rack = 0

while clotes_in_box:
    current_piece = clotes_in_box.popleft()
    if current_rack + current_piece <= capacity:
        current_rack += current_piece
    else:
        number_of_racks += 1
        current_rack = current_piece

print(number_of_racks)
