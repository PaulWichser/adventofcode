import fileimp

def countint(imglist,num):
    count = 0
    for i in range(len(imglist)):
        for j in range(len(imglist[i])):
            if imglist[i][j] == num:
                count += 1
    return count

def imgbuild(imgdict):
    imglist = imgdict['L0']
    for i in range(len(imgdict)):
        for j in range(len(imgdict['L%i' % i])):
            for k in range(len(imgdict['L%i' % i][j])):
                if imglist[j][k] == 2:
                    imglist[j][k] = imgdict['L%i' % i][j][k]
    return imglist

def imgdisplay(imglist):
    img = []
    for i in range(len(imglist)):
        list = []
        for j in range(len(imglist[i])):
            if imglist[i][j] == 1:
                list.append('#')
            else:
                list.append('.')
        print(list)


image = fileimp.sifimp('day8-1input.txt',25,6)

zeros = []
for i in range(len(image)):
    zeros.append(countint(image['L%i' % i],0))
mindex = zeros.index(min(zeros))
ans = countint(image['L%i' % mindex],1)*countint(image['L%i' % mindex],2)
print(ans)

imgdisplay(imgbuild(image))
