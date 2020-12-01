#Solution for https://adventofcode.com/2019/day/3
def wireimp(filename):
    with open(filename,'r') as file:
        wires = {}
        x=1
        for line in file:
            line = line.rstrip('\n')
            list = line.split(',')
            wires['wire%i' % x] = list
            # print(len(wires))
            x += 1
    print("Imported wire dictionary of length %i" % len(wires))
    return wires

def cartwire(list):
    outlist = []
    coords = [0,0,0]
    for x in range(len(list)):
        #convert strings to cartesian coords
        dir = list[x][0]
        list[x] = int(list[x].replace(dir,''))
        for i in range(list[x]):
            if dir == 'R':
                coords[0] = coords[0]+1
            elif dir == 'L':
                coords[0] = coords[0]-1
            elif dir == 'U':
                coords[1] = coords[1]+1
            elif dir == 'D':
                coords[1] = coords[1]-1
            else:
                print('Unexpected direction of %s' % dir)
                quit()
            # print(coords)
            coords[2] = coords[2]+1
            outlist.append(coords.copy())
            # print(outlist)
    # print(outlist)
    return outlist

def cross(list1,list2):
    crosslist = []
    length = len(list1)*len(list2)
    counter = 0
    print('Checking %i possibilities for crossed wires' % length)
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i][0] == list2[j][0] and list1[i][1] == list2[j][1]:
                totdist = list1[i][2]+list2[j][2]
                crosslist.append([list1[i][0],list1[i][1],totdist])
            counter +=1
            if not (counter%10000000):
                print('%i' % ((counter/length)*100))
    return crosslist

def closecross(inlist):  #returns min Manhattan distance of cross list
    crosslist = inlist.copy()
    for i in range(len(crosslist)):
        crosslist[i] = abs(crosslist[i][0]) + abs(crosslist[i][1])
    print(crosslist)
    return min(crosslist)

def wirelen(inlist):    #returns total added wire length from origin
    crosslist = inlist.copy()
    for i in range(len(crosslist)):
        crosslist[i] = crosslist[i][2]
    print(crosslist)
    return min(crosslist)

def test(filename,closeans,lenans):
    testdict = wireimp(filename)
    crosslist = cross(cartwire(testdict['wire1']),cartwire(testdict['wire2']))
    if closecross(crosslist) == closeans and wirelen(crosslist) == lenans:
        print('Test cross check successful!')
    else:
        print('Test cross check failure!')
        quit()

test('day3-1test2.txt',159,610)
test('day3-1test.txt',135,410)

wiredict = wireimp('day3-1input.txt')
print(wirelen(cross(cartwire(wiredict['wire1']),cartwire(wiredict['wire2']))))
