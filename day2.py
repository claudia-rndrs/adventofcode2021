def dive():
    testCourse = ["forward 5","down 5","forward 8","up 3","down 8","forward 2"]

    file = open("data/plannedcourse.txt")
    course = file.read().split("\n")
    file.close()

    xPos = int(0)
    depth = int(0)
    aim = int(0)

    for pos in course:
        direction, movement = pos.split()

        if direction == "forward":
            val = int(movement)
            xPos += val
            
            if aim > 0 :
                depth += (val * aim)
            
        elif direction == "down":
            aim += int(movement)

        elif direction == "up":
            aim -= int(movement)

    return xPos * depth


finalPos = dive()
print(finalPos)