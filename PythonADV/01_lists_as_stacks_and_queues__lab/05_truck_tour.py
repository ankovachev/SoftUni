from collections import deque

results = deque()


pumps = int(input())  # NUmber of petrol pumps

for each in range(pumps):
    current_pump = input().split()
    petrol_result = int(current_pump[0]) - int(current_pump[1])
    results.append(petrol_result)

for start_pump in range(pumps):
    current_result = 0
    success = True
    for each in results:
        current_result += each
        if current_result < 0:
            results.append(results.popleft())
            success = False
            break
    if success:
        print(start_pump)
        break
