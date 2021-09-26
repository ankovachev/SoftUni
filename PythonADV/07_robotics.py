from datetime import datetime, timedelta
import sys
from collections import deque
from io import StringIO


def give_me_free_robot(robots, time):
    for el_robot in robots:
        if robots[el_robot][1] <= time:
            return el_robot
    return "Not_Founded"

#
# input1 = """ROB-15;SS2-10;NX8000-3
# 8:00:00
# detail
# glass
# wood
# apple
# End
# """
#
# input2 = """ROB-8
# 7:59:59
# detail
# glass
# wood
# sock
# End
# """
#
# sys.stdin = StringIO(input1)

rob_input = input().split(";")
#  Convert time to numbers
start_input_time = input()
hh, mm, ss = start_input_time.split(":")
hh = int(hh)
mm = int(mm)
ss = int(ss)
start_time = datetime(1, 1, 1, hh, mm, ss)

rob_dict = {}
robots_queue = deque()
products = deque()

for each in rob_input:
    each_elem = each.split("-")
    robot, proc_time = each_elem[0], int(each_elem[1])
    rob_dict[robot] = [proc_time, 0]
    robots_queue.append(robot)

current_time = 1

while True:
    command = input()
    if command == "End":
        break
    products.append(command)

while products:
    next_product = products.popleft()
    free_rob = give_me_free_robot(rob_dict, current_time)
    if free_rob == "Not_Founded":
        products.append(next_product)
    else:
        rob_dict[free_rob][1] = current_time + rob_dict[free_rob][0]
        time_for_print = timedelta(0, current_time) + start_time
        print(f"{free_rob} - {next_product} [{time_for_print.time()}]")
    current_time += 1
