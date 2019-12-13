import fileimp


def bestaster(asters):
    for i in range(len(asters)):
        for j in range(len(asters[i])):
            if asters[i][j] == 1:
                slopes = {}
                for k in range(len(asters)):
                    for l in range(len(asters[k])):
                        if asters[k][l] == 1:
                            slopes['%']

asters = fileimp.asterimp('day10-1test1.txt')
