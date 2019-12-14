import fileimp
import math

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
                            elif y1-y0 <= 0 and x1-x0 <= 0: q = 3
                            else: q = 4
                            if q == 1 and x1-x0 == 0: slope = 999999999
                            elif q == 3 and x1-x0 == 0: slope = -999999999
                            else:
                                slope = (y1-y0)/(x1-x0)
                            slopes.setdefault(q, {})
                            slopes[q].setdefault(slope, {})
                            distance = math.sqrt(((x1-x0)**2)+((y1-y0)**2))
                            slopes[q][slope].setdefault(distance, [])
                            slopes[q][slope][distance].append([x1,y1])
            slopescount = 0
            for i in slopes:
                for j in slopes[i]:
                    # for k in slopes[i][j]:
                        # for l in slopes[i][j][k]:
                    slopescount += 1
            if slopescount > maxloc[0]:
                maxloc = [slopescount,x0,y0]
                maxslopes = slopes.copy()
            # print(slopes)
    print('The best asteroid is at (%i,%i), with %i others visible.' % (maxloc[1],maxloc[2],maxloc[0]))
    return maxloc, maxslopes



if bestaster(fileimp.asterimp('day10-1test1.txt'))[0][0] != 35 or bestaster(fileimp.asterimp('day10-1test2.txt'))[0][0] != 41 or bestaster(fileimp.asterimp('day10-1test3.txt'))[0][0] != 210:
    print('Tests failed!')
    quit()

def laser(filename):
    loc, slopes = bestaster(fileimp.asterimp(filename))

#find best asteroid (23,19) (loc[1],loc[2])
#find distance to each other asteroid (sqrt((x1-x0)^2+(y1-y0)^2)) slopes[q][slope][distance]
#starting straight up (slope 999999999) in q1, shoot closest min(slopes[q][slope])
#increment smaller slopes, shoot closest
#keep counter, @ 199: x1*100 + y1
