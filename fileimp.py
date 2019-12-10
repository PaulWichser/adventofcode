def intimp(filename):
    with open(filename,'r') as file:
        for line in file:
            line = line.rstrip('\n')
            list = line.split(',')
            # print(len(list))
        for x in range(len(list)):
            list[x] = int(list[x])
    print("Imported int list of length %i" % len(list))
    return list

def wireimp(filename):
    with open(filename,'r') as file:
        wires = []
        for line in file:
            line = line.rstrip('\n')
            list = line.split(',')
            wires.append(list)
            print(len(wires))
    return wires
