import fileimp

# import grid as list of lists
# traverse grid input(filename, dx, dy)
#   increment x and y by dx and dy
#   check if new x pos is outside of grid
#       reset grid position for repeating grid
#   count 1s as trees, do not count 0s

def counttrees(treelist, dx, dy):
#    print('treelist: max Y =', len(treelist)-1, ', max X =', len(treelist[0])-1)
    x = 0
    y = 0
    treecount = 0
    while y < len(treelist):
#        print('line =', y, ', column =', x, ', value = ', treelist[y][x], ', treecount =', treecount)
        treecount = treecount + treelist[y][x]
        if (x + dx) > len(treelist[y])-1:         #grids repeat, expect x > width
            x = dx - (len(treelist[y]) - (x))    #reset grid position for repeating grid
        else:
            x = x + dx
        y = y + dy
    return treecount

if(\
counttrees(fileimp.gridimp('d03.test.txt'),1,1) *\
counttrees(fileimp.gridimp('d03.test.txt'),3,1) *\
counttrees(fileimp.gridimp('d03.test.txt'),5,1) *\
counttrees(fileimp.gridimp('d03.test.txt'),7,1) *\
counttrees(fileimp.gridimp('d03.test.txt'),1,2))\
!= 336:
    print("Test Failed!")
    quit()

#print('number of trees =', counttrees(fileimp.gridimp('d03.input.txt'),3,1))
trees =\
counttrees(fileimp.gridimp('d03.input.txt'),1,1) *\
counttrees(fileimp.gridimp('d03.input.txt'),3,1) *\
counttrees(fileimp.gridimp('d03.input.txt'),5,1) *\
counttrees(fileimp.gridimp('d03.input.txt'),7,1) *\
counttrees(fileimp.gridimp('d03.input.txt'),1,2)
print('number of trees =', trees)
