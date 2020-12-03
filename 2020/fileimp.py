def listimp(filename):
    with open(filename,'r') as file:
        list = []
        for line in file:
            line = line.rstrip('\n')
            list.append(line)
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

def sifimp(filename,w,h):
    list = []
    with open(filename,'r') as file:
        for line in file:
            line = line.rstrip('\n')
            for ch in line:
                list.append(int(ch))
    image = {}
    line = []
    i = 0
    j = 0
    k = 0
    l = 0
    while i < len(list):
        image['L%i' % l] = []
        j = 0
        while j < h:
            # image['L%i' % l][j] = []
            line = []
            k = 0
            while k < w:
                line.append(list[i])
                print(line)
                i += 1
                k += 1
            image['L%i' % l].append(line.copy())
            print(image)
            j += 1
        l += 1
    return image

def asterimp(filename):
    asterlist = []
    with open(filename,'r') as file:
        i = 0
        for line in file:
            line = line.rstrip('\n')
            j = 0
            linelist = []
            for ch in line:
                if ch == '.':
                    linelist.append(0)
                elif ch == '#':
                    linelist.append(1)
                else:
                    print('Unexpected character at %i,%i' % (i,j))
                    quit()
            asterlist.append(linelist)
    return asterlist

def fftimp(filename):
    list = []
    with open(filename,'r') as file:
        for line in file:
            line = line.rstrip('\n')
            for ch in line:
                list.append(int(ch))
    return list
