def dive():
    file = open("data/plannedcourse.txt")
    course = file.read().split("\n")
    file.close()

    xPos = int(0)
    depth = int(0)

    for pos in course:
        direction, movement = pos.split()

        if direction == "forward":
            xPos += int(movement)
        elif direction == "down":
            depth += int(movement)
        elif direction == "up":
            depth -= int(movement)

    return xPos * depth


finalPos = dive()
print(finalPos)