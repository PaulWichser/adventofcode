import fileimp

patt = [0,1,0,-1]

# import input list
# generate pattern list
#   pattern list repeats through patt until list is input+1 long
#   pattern list generates based on number of times through so that each patt member gets i+1 entries per iteration
#   lose first pattern list item
# multiply input list item to corresponding patt list item
# add each multiplied item and abs(modal 10)
# build new input list as long as input and repeat for required steps

def pattlistgen(patt,step,inlength):
    list = []
    while len(list) <= inlength:
        for i in patt:
            j = 0
            while j <= step:
                list.append(i)
                j+=1

    list.pop(0)
    # print(len(list))
    return list

def listcalc(inlist):
    outlist = []
    p = 0
    for i in range(len(inlist)):
        pattlist = pattlistgen(patt,i,len(inlist))
        linetot = 0
        for j in range(len(inlist)):
            linetot += (inlist[j] * pattlist[j])
        outlist.append(abs(linetot) % 10)
        p2 = p
        p = int(i/len(inlist))
        if p2 != p:
            print(p)
    # print(outlist)
    return outlist

def firsteight(inlist,steps):
    for i in range(steps):
        inlist = listcalc(inlist)
    output = 0
    for i in range(8):
        output += inlist[8 - (i+1)]*(10**i)
    return output

def whicheight(inlist,steps):
    for i in range(steps):
        inlist = listcalc(inlist)
        print(i)
    output = 0
    for i in range(8):
        index = offset + 8 - i + 1
        print(len(inlist))
        print(index)
        output += inlist[index]*(10**i)
    return output

def newlist(inlist,repeats):
    outlist = []
    for i in range(repeats):
        for j in inlist:
            outlist.append(j)
    print(len(outlist))
    return outlist

def testfile(filename,ans,repeats):
    test = whicheight(newlist(fileimp.fftimp(filename),repeats),100)
    if test != ans:
        print(test)
        print('Test failed')
        quit()

testfile('day16-1test1.txt',84462026,10000)
testfile('day16-1test2.txt',78725270,10000)
testfile('day16-1test3.txt',53553731,10000)



thislist = newlist(fileimp.fftimp('day16-1input.txt'),10000)

print(whicheight(thislist,100,offset))

# print(firsteight(fileimp.fftimp('day16-1input.txt'),100))
