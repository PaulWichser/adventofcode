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

def positletters(list):
    passwordcount = 0
    for i in range(len(list)):
        lettercount = 0
        success = 0
        for j in list[i][3]:
            lettercount = lettercount + 1
            if ((j == list[i][2]) and ((lettercount == list[i][0]) or (lettercount == list[i][1]))):
                success = success + 1
        if success == 1:
            print(i,list[i][0],list[i][1],lettercount,j,list[i][2],passwordcount+1)
            passwordcount = passwordcount + 1
    print(passwordcount,'successful passwords')
    return passwordcount

if positletters(parsepasslist(fileimp.listimp('d02.test.txt'))) != 1:
    print("Test Failed!")
    quit()

x = positletters(parsepasslist(fileimp.listimp('d02.input.txt')))
