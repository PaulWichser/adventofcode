def listimp(filename):
    with open(filename,'r') as file:
        list = []
        for line in file:
            line = line.rstrip('\n')
            list.append(int(line))
    return list

def intimp(filename):
    list=[]
    with open(filename,'r') as file:
        for line in file:
            line = line.rstrip('\n')
            inlist = line.split(',')
            # print(len(list))
            for x in range(len(inlist)):
                list.append(int(inlist[x]))
    print("Imported int list of length %i" % len(list))
    return list

def wireimp(filename):
    with open(filename,'r') as file:
        wires = {}
        x=1
        for line in file:
            line = line.rstrip('\n')
            list = line.split(',')
            wires['wire%i' % x] = list
            print(len(wires))
            x += 1
    print("Imported wire dictionary of length %i" % len(wires))
    return wires
