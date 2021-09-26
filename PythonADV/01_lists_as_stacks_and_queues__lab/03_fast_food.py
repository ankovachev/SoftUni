import sys
from collections import deque
from io import StringIO

# input1 = """348
# 20 54 30 16 7 9
# """
# input2 = """499
# 57 45 62 70 33 90 88 76 100 50
# """
#
# sys.stdin = StringIO(input2)

quantity_of_the_food = int(input())
customer_input = input().split()
customers = deque()
[customers.append(int(each)) for each in customer_input]
current_quantity = quantity_of_the_food
print(max(customers))
while customers:
    current_order = customers.popleft()
    left_food = current_quantity - current_order
    if left_food < 0:
        customers.appendleft(current_order)
        break
    current_quantity -= current_order

if customers:
    print(f"Orders left: {' '.join([str(each) for each in customers])}")
else:
    print("Orders complete")

