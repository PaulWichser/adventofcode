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
        wires = {}
        x=1
        for line in file:
            line = line.rstrip('\n')
            list = line.split(',')
            wires['wire%i' % x] = list
<<<<<<< HEAD
            # print(len(wires))
=======
            print(len(wires))
>>>>>>> 1631137c269fdb829e0896b69b34371fd5f2e87b
            x += 1
    print("Imported wire dictionary of length %i" % len(wires))
    return wires
