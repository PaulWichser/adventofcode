import fileimp


def bestaster(asters):
    maxloc = [0,0,0]
    for i in range(len(asters)):
        for j in range(len(asters[i])):
            slopes = {}
            if asters[i][j] == 1:
                for k in range(len(asters)):
                    for l in range(len(asters[k])):
                        if asters[k][l] == 1:
                            if i-k == 0:
                                slope = 999999999
                                if j-l < 0:
                                    slope = slope*(-1)
                            else:
                                slope = (j-l)/(i-k)
                            slopes.setdefault('%f' % slope, [])
                            slopes['%f' % slope].append([l,k])
            if len(slopes) > maxloc[0]:
                maxloc = [len(slopes),j,i]
            # print(slopes)
    print('The best asteroid is at (%i,%i), with %i others visible.' % (maxloc[1],maxloc[2],maxloc[0]))
    return maxloc



if bestaster(fileimp.asterimp('day10-1test1.txt'))[0] != 35 or bestaster(fileimp.asterimp('day10-1test2.txt'))[0] != 41 or bestaster(fileimp.asterimp('day10-1test3.txt'))[0] != 210:
    print('Tests failed!')
    quit()
