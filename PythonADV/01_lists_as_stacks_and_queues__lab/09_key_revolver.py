from collections import deque

safe_is_open = False
bullets = deque()
locks = deque()

price_of_a_bullet = int(input())        # price of each bullet – an integer in the range [0-100]
size_of_gun_barrel = int(input())       # size of the gun barrel – an integer in the range [1-5000]
bullets_input = input().split()         # bullets – a space-separated integer sequence with [1-100] integers
locks_input = input().split()           # the locks – a space-separated integer sequence with [1-100] integers
value_of_intelligence = int(input())    # the value of the intelligence – an integer in the range [1-100000]

[bullets.append(int(each)) for each in bullets_input]
[locks.append(int(each)) for each in locks_input]

barrel = size_of_gun_barrel
while True:
    current_bullet = bullets.pop()
    barrel -= 1
    current_lock = locks[0]
    if current_bullet <= current_lock:
        locks.popleft()
        print("Bang!")
    else:
        print("Ping!")
    if barrel == 0 and bullets:
        print("Reloading!")
        barrel = size_of_gun_barrel
    if not locks:
        safe_is_open = True
        break
    if not bullets:
        break


if safe_is_open:
    money_earned = value_of_intelligence - ((len(bullets_input) - len(bullets)) * price_of_a_bullet)
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
# That's all folks
