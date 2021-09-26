from collections import deque

cars = deque()

green_light = int(input())
free_window = int(input())
passed_cars = 0
current_green_limit = 0
is_crash_happened = False

while True:
    command = input()
    if command == "END":
        print("Everyone is safe.")
        print(f"{passed_cars} total cars passed the crossroads.")
        exit()
    if command != "green":
        cars.appendleft(command)
        continue
    current_green_limit = green_light
    while cars:
        current_car = cars.pop()
        current_green_limit -= len(current_car)
        current_yelow_limit = current_green_limit + free_window
        if current_green_limit < 0:
            if current_yelow_limit < 0:
                print("A crash happened!")
                hit_to_letter = current_car[abs(current_green_limit)-1]
                print(f"{current_car} was hit at {hit_to_letter}.")
                exit()
            passed_cars += 1
            break
        elif current_green_limit == 0:
            passed_cars += 1
            break
        else:
            passed_cars += 1
