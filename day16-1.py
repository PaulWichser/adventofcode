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
    return list

def listcalc(inlist):
    outlist = []
    for i in range(len(inlist)):
        pattlist = pattlistgen(patt,i,len(inlist))
        linetot = 0
        for j in range(len(inlist)):
            linetot += (inlist[j] * pattlist[j])
        outlist.append(abs(linetot) % 10)
    # print(outlist)
    return outlist

def firsteight(inlist,steps):
    for i in range(steps):
        inlist = listcalc(inlist)
    output = 0
    for i in range(8):
        output += inlist[8 - (i+1)]*(10**i)
    return output

def testfile(filename,ans):
    test = firsteight(fileimp.fftimp(filename),100)
    if test != ans:
        print(test)
        print('Test failed')
        quit()

testfile('day16-1test1.txt',24176176)
testfile('day16-1test2.txt',73745418)
testfile('day16-1test3.txt',52432133)

print(firsteight(fileimp.fftimp('day16-1input.txt'),100))
