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

def getvals(listdata,code,loc,params):
    mode = [code[2],code[1],code[0]]
    ploc = [loc+1,loc+2,loc+3]
    for i in range(params):
        vals[i] = getvalue(listdata,mode[i],ploc[i])
    return vals

def intop3(listdata,code,loc,params):
    listd = getvals(listdata,code,loc,params)
    listdata[listdata[loc+1]] = int(input('Enter intcomp value: '))

def intop4(listdata,code,loc,params):
    print('Intcomp value output: %i' % listdata[listdata[loc+1]])
    listd = getvals(listdata,code,loc,params)
    if listd[0] != 0:
        if listdata[x+2] == 99:
            print('Diagnostic code: %i' % listd[0])
            quit()
        else:
            print('Unexpected value %i at location %i' % (listd[0],listdata[x+1]))
            quit()


def intcomp(listdata):
    x = 0
    while x < len(listdata):
        print('x = %i' % x)
        code = getcode(listdata[x])
        op = code[-1] + (code[-2] * 10)
        pval1 = getvalue(listdata,mode1,ploc1)
        listd1 = listdata[pval1]
        params = 1

        if op == 99:
            break

        elif op == 3:
            listop3(listdata,code,x,params)
            x += 

        elif op == 4:
            listop4(listdata,code,x,params)
            x += 2

        else:
            params = 2
            pval2 = getvalue(listdata,mode2,ploc2)
            listd2 = listdata[pval2]

            if op == 5:
                if listd1 != 0:
                    x += listd2
                else:
                    x +=

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
    x += params+1
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
