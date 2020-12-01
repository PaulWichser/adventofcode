import fileimp


def bestaster(asters):
    maxloc = [0,0,0]
    for y0 in range(len(asters)):
        for x0 in range(len(asters[y0])):
            slopes = {}
            if asters[y0][x0] == 1:
                for y1 in range(len(asters)):
                    for x1 in range(len(asters[y1])):
                        if asters[y1][x1] == 1:
                            if y1-y0 >= 0 and x1-x0 >= 0: q = 1
                            elif y1-y0 <= 0 and x1-x0 > 0: q = 2
                            elif y1-y0 <= 0 and x1-x0 < 0: q = 3
                            else: q = 4
                            if x1-x0 == 0: slope = 999999999
                            else:
                                slope = (y1-y0)/(x1-x0)
                            slopes.setdefault('%i,%f' % (q,slope), [])
                            slopes['%i,%f' % (q,slope)].append([x1,y1])
            if len(slopes) > maxloc[0]:
                maxloc = [len(slopes),x0,y0]
                maxslopes = slopes.copy()
            # print(slopes)
    print('The best asteroid is at (%i,%i), with %i others visible.' % (maxloc[1],maxloc[2],maxloc[0]))
    return maxloc, maxslopes



if bestaster(fileimp.asterimp('day10-1test1.txt'))[0][0] != 35 or bestaster(fileimp.asterimp('day10-1test2.txt'))[0][0] != 41 or bestaster(fileimp.asterimp('day10-1test3.txt'))[0][0] != 210:
    print('Tests failed!')
    quit()

bestaster(fileimp.asterimp('day10-1input.txt'))
