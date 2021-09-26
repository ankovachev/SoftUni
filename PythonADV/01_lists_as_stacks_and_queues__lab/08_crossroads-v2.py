# import sys
from collections import deque
# from io import StringIO

# input1 = """9
# 3
# Mercedes
# Hummer
# green
# Hummer
# Mercedes
# green
# END
# """
# input2 = """10
# 5
# Mercedes
# green
# Mercedes
# BMW
# Skoda
# green
# END
# """
#
# sys.stdin = StringIO(input2)

green = int(input())
yelow = int(input())
crash = False
crashed_car = ""
character_hit = ""
cars = deque()
total_cars_passed = 0

line = input()
while line != "END":
    if line != "green":
        cars.append(line)
        line = input()
        continue
    # Green light is lighting - Старт на зелено започващо от нула
    rest_of_green = green
    #  Стартира зелен сигнал и Докато има коли - преминават
    while cars:
        current_car = cars.popleft()
        len_cc = len(current_car)
        if rest_of_green > len_cc:
            total_cars_passed += 1
            rest_of_green -= len_cc
        elif rest_of_green == len_cc:
            total_cars_passed += 1
            #  Понеже зеления светофар се е изчерпал, прекъсваме цикъла и чакаме нова копманда
            break
        else:
            #  Зеления сигнал се сменя с жълт, но колата още е кръстовището
            #  Ako остатъка от зелено плюс цялото жълно не стигнат - катастрофа
            if rest_of_green + yelow < len_cc:
                crash = True
                crashed_car = current_car
                character_hit = crashed_car[rest_of_green + yelow]
            #  Ako остатъка от зелено плюс цялото жълно стигнат - колата минава, но друга не тръгва - прекъсваме цикъла
            #  и отиваме да чакаме нова команда
            else:
                total_cars_passed += 1
            break
        if crash:
            break
    #  Read next input
    line = input()

if crash:
    print("A crash happened!")
    print(f"{crashed_car} was hit at {character_hit}.")
else:
    print("Everyone is safe.")
    print(f"{total_cars_passed} total cars passed the crossroads.")
