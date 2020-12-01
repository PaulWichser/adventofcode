import fileimp
#Solution for https://adventofcode.com/2019/day/5
testdata = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
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
    try:
        if mode == 0:
            # print(listdata[loc])
            return listdata[loc]
        elif mode == 1:
            # print(loc)
            return loc
        else:
            print('Unrecognized mode: %i' % mode)
            quit()
    except:
        listdata.append(-1)
        return -1



def intcomp(listdata):
    x = 0
    while x < len(listdata):
        print('x = %i' % x)
        code = getcode(listdata[x])
        op = code[-1] + (code[-2] * 10)
        mode1 = code[-3]
        mode2 = code[-4]
        mode3 = code[-5]
        ploc1 = x+1
        ploc2 = x+2
        ploc3 = x+3
        pval1 = getvalue(listdata,mode1,ploc1)
        listd1 = listdata[pval1]

        if op == 99:
            break

        elif op == 3:
            listdata[listdata[x+1]] = int(input('Enter intcomp value: '))
            x += 2

        elif op == 4:
            print('Intcomp value output: %i' % listdata[listdata[x+1]])
            if listd1 != 0:
                if listdata[x+2] == 99:
                    print('Diagnostic code: %i' % listd1)
                    quit()
                else:
                    print('Unexpected value %i at location %i' % (listd1,listdata[x+1]))
                    quit()
            x += 2

        else:
            pval2 = getvalue(listdata,mode2,ploc2)
            listd2 = listdata[pval2]

            if op == 5:
                if listd1 != 0:
                    x += listd2
                else:
                    x += 3

            elif op == 6:
                if listd1 == 0:
                    x += listd2
                else:
                    x += 3

            else:
                pval3 = getvalue(listdata,mode3,ploc3)
                listd3 = listdata[pval3]

                if op == 1:
                    listdata[pval3] = listd2 + listd1
                    print('%i at listdata[%i]' % (listd3,pval3))
                    x += 4
                    # print(listdata)

                elif op == 2:
                    listdata[pval3] = listd2 * listd1
                    print('%i at listdata[%i]' % (listd3,pval3))
                    x += 4
                    # print(listdata)

                elif op == 7:
                    if listd1 < listd2:
                        listdata[pval3] = 1
                        print('1 at listdata[%i]' % pval3)
                    else:
                        listdata[pval3] = 0
                        print('0 at listdata[%i]' % pval3)
                    x += 4

                elif op == 8:
                    if listd1 == listd2:
                        listdata[pval3] = 1
                        print('1 at listdata[%i]' % pval3)
                    else:
                        print('0 at listdata[%i]' % pval3)
                        listdata[pval3] = 0
                    x += 4

                else:
                    print('Unexpected opcode: %i at %i' % (listdata[x], x))
                    x += 4
                    break

    print(listdata)
    print('Intcode computer position 0 = %i' % listdata[0])
    return listdata[0]

print('If input < 8, output should be 999. If input = 8, output should be 1000. If input > 8, output should be 1001')
intcomp(testdata)

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
