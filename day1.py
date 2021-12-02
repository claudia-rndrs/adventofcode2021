def sonarSweep():
    file = open("data/sonardata.txt")
    data = file.read().split()
    file.close()

    count = int(0)
    previous = int(0)

    for number in data:
        if(previous and int(number) > previous):
            count +=1
        
        previous = int(number)
    
    return count

finalcount = sonarSweep()
print(finalcount)
