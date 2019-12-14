import fileimp

def countint(imglist,num):
    count = 0
    for i in range(len(imglist)):
        for j in range(len(imglist[i])):
            if imglist[i][j] == num:
                count += 1
    return count

image = fileimp.sifimp('day8-1input.txt',25,6)
zeros = []
for i in range(len(image)):
    zeros.append(countint(image['L%i' % i],0))
mindex = zeros.index(min(zeros))
ans = countint(image['L%i' % mindex],1)*countint(image['L%i' % mindex],2)
print(ans)
