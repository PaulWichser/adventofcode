import fileimp
#Solution for https://adventofcode.com/2019/day/5
testdata = [1,9,10,3,2,3,11,0,99,30,40,50]
# inputdata = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,6,19,23,2,23,6,27,2,6,27,31,2,13,31,35,1,10,35,39,2,39,13,43,1,43,13,47,1,6,47,51,1,10,51,55,2,55,6,59,1,5,59,63,2,9,63,67,1,6,67,71,2,9,71,75,1,6,75,79,2,79,13,83,1,83,10,87,1,13,87,91,1,91,10,95,2,9,95,99,1,5,99,103,2,10,103,107,1,107,2,111,1,111,5,0,99,2,14,0,0]

def getcode(intnum):
    strnum = str(intnum)
    code = []
    for i in range(len(strnum)):
        code.insert(i,int(strnum[i]))
    while len(code) < 5:
        code.insert(0,0)
    print('code:')
    print(code)
    return code

def getvalue(listdata,mode,loc):
    print('mode: %i, loc: %i' % (mode,loc))
    if mode == 0:
        print(listdata[loc])
        return listdata[loc]
    elif mode == 1:
        print(loc)
        return loc
    else:
        print('Unrecognized mode: %i' % mode)
        quit()

def intcomp(listdata):
    x = 0
    while x < len(listdata):
        print('x = %i' % x)
        code = getcode(listdata[x])
        op = code[len(code)-1] + (code[len(code)-2] * 10)

        if op == 1:
            listdata[getvalue(listdata,code[len(code)-5],x+3)] = listdata[getvalue(listdata,code[len(code)-4],x+2)] + listdata[getvalue(listdata,code[len(code)-3],x+1)]
            x += 4
            print(listdata)

        elif op == 2:
            listdata[getvalue(listdata,code[len(code)-5],x+3)] = listdata[getvalue(listdata,code[len(code)-4],x+2)] * listdata[getvalue(listdata,code[len(code)-3],x+1)]
            x += 4
            print(listdata)

        elif op == 3:
            listdata[listdata[x+1]] = int(input('Enter intcomp value: '))
            x += 2

        elif op == 4:
            print('Intcomp value output: %i' % listdata[listdata[x+1]])
            if listdata[getvalue(listdata,code[len(code)-3],x+1)] != 0:
                if listdata[x+2] == 99:
                    print('Diagnostic code: %i' % listdata[getvalue(listdata,code[len(code)-3],x+1)])
                    quit()
                print('Unexpected value %i at location %i' % (listdata[getvalue(listdata,code[len(code)-3],x+1)],listdata[x+1]))
                quit()
            x += 2

        elif op == 99:
            break

        else:
            print('Unexpected opcode: %i at %i' % (listdata[x], x))
            x += 4
            break

    print(listdata)
    print('Intcode computer position 0 = %i' % listdata[0])
    return listdata[0]

if intcomp(testdata) == 3500:
     print('Intcode computer test successful')
else:
     print('Intcode computer test failure')
     quit()

filename = input('Enter data file name: ')
listdata = fileimp.intimp(filename)
intcomp(listdata)

# for noun in range(100):
#     for verb in range(100):
#         indat = inputdata.copy()
#         indat[1] = noun
#         indat[2] = verb
#         if intcomp(indat) == 19690720:
#             print('Final intcode: %s' % indat)
#             print('noun=%i' % noun)
#             print('verb=%i' % verb)
#             quit()
