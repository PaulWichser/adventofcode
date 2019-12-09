#Solution for https://adventofcode.com/2019/day/2
testdata = [1,9,10,3,2,3,11,0,99,30,40,50]
inputdata = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,6,19,23,2,23,6,27,2,6,27,31,2,13,31,35,1,10,35,39,2,39,13,43,1,43,13,47,1,6,47,51,1,10,51,55,2,55,6,59,1,5,59,63,2,9,63,67,1,6,67,71,2,9,71,75,1,6,75,79,2,79,13,83,1,83,10,87,1,13,87,91,1,91,10,95,2,9,95,99,1,5,99,103,2,10,103,107,1,107,2,111,1,111,5,0,99,2,14,0,0]
inputdata[1] = 12
inputdata[2] = 2
def intcomp(listdata):
    x = 0
    while listdata[x] != 99:
        if listdata[x] == 1:
            listdata[listdata[x+3]] = listdata[listdata[x+1]] + listdata[listdata[x+2]]
            x += 4
#            print(listdata)
        elif listdata[x] == 2:
            listdata[listdata[x+3]] = listdata[listdata[x+1]] * listdata[listdata[x+2]]
            x += 4
#            print(listdata)
        else:
            print('Unexpected opcode: %i' % x)
            quit()

    print('Intcode computer position 0 = %i' % listdata[0])
    return listdata[0]

if intcomp(testdata) == 3500:
    print('Intcode computer test successful')
else:
    print('Intcode computer test failure')
    quit()

intcomp(inputdata)
