def sonarSweep():
    file = open("data/sonardata.txt")
    data = file.read().split()
    file.close()

    count = int(0)
    previous = int(0)
    length = len(data)

    for i in range(0,length -2):
        a = int(data[i])
        b = int(data[i+1])
        c = int(data[i+2])
        sum = a + b + c

        if(previous and sum > previous): 
            count +=1
        
        previous = sum
    
    return count

finalcount = sonarSweep()
print(finalcount)