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
    coords = [0,0]
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
            outlist.append(coords.copy())
            # print(outlist)
    # print(outlist)
    return outlist

def closecross(list1,list2):
    crosses = []
    length = len(list1)*len(list2)
    counter = 0
    print('Checking %i possibilities for crossed wires' % length)
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                crosses.append(list1[i])
            counter +=1
            if not (counter%10000000):
                print('%i' % ((counter/length)*100))
    for i in range(len(crosses)):
        crosses[i] = abs(crosses[i][0]) + abs(crosses[i][1])
    print(crosses)
    return min(crosses)

def test(filename,ans):
    testdict = wireimp(filename)
    if closecross(cartwire(testdict['wire1']),cartwire(testdict['wire2'])) == ans:
        print('Test cross check successful!')
    else:
        print('Test cross check failure!')
        quit()

test('day3-1test2.txt',159)
test('day3-1test.txt',135)

wiredict = wireimp('day3-1input.txt')
print(closecross(cartwire(wiredict['wire1']),cartwire(wiredict['wire2'])))
