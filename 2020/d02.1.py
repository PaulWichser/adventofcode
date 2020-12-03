import fileimp

# import list of strings
# split strings into min, max, letter, and password
    #string.split('')
# count letter in password
# check within min max
# iterate count

def parsepasslist(list):
    returnlist = []
    for i in range(len(list)):
        onepasslist = []
        temp = list[i].split(' ')
        onepasslist.append(int(temp[0].split('-')[0]))
        onepasslist.append(int(temp[0].split('-')[1]))
        onepasslist.append(temp[1].split(':')[0])
        onepasslist.append(temp[2])
        returnlist.append(onepasslist)
#    print(returnlist)
    return returnlist

def countletters(list):
    passwordcount = 0
    for i in range(len(list)):
        lettercount = 0
        for j in list[i][3]:
            if j == list[i][2]:
                lettercount = lettercount + 1
        if list[i][0] <= lettercount <= list[i][1]:
            passwordcount = passwordcount + 1
    return passwordcount

if countletters(parsepasslist(fileimp.listimp('d02.test.txt'))) != 2:
    print("Test Failed!")
    quit()

x = countletters(parsepasslist(fileimp.listimp('d02.input.txt')))
print(x,'successful passwords')
