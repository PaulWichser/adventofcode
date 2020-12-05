import fileimp

# listimp data as list
# iterate through list of strings, concatenating into larger string
#   if list entry is blank '', end string, start over
# search strings for byr, iyr, eyr, hgt, hcl, ecl, pid, cid (optional)
# if all but cid, valid, return list of valid by number of entries
# convert valid list of strings to list of dicts
# pass dict values by name to entry validators, return 1 for valid
# count if all entries valid, count

def cleanlist(list):
    returnlist = []
    string = ""
    for i in list:
        if i == '':
            returnlist.append(string.lstrip(" "))
            string = ""
        else:
            string = string + " " + i
    returnlist.append(string.lstrip(" "))
    print(returnlist)
    return returnlist

def dictlist(list): #converts list of strings to dicts
    returnlist = []
    for x in list:
        print(x)
        Dict = dict((x.strip(), y.strip()) for x, y in (element.split(':') for element in x.split(' ')))
        returnlist.append(Dict)
    return returnlist

def valbyr(string):
    if string.isdigit():
        if 1920 <= int(string) <= 2002:
            return 0
    else:
        print("bad byr")
        return 1

def valiyr(string):
    if string.isdigit():
        if 2010 <= int(string) <= 2020:
            return 0
    else:
        print("bad iyr")
        return 1

def valeyr(string):
    if string.isdigit():
        if 2020 <= int(string) <= 2030:
            return 0
    else:
        print("bad eyr")
        return 1

def valhgt(string):
    if string.find("cm") != -1:
        c = string.rstrip("cm")
    if string.find("in") != -1:
        i = string.rstrip("in")
    if c.isdigit():
        if 150 <= int(c) <= 193:
            return 0
    if i.isdigit():
        if 59 <= int(i) <= 76:
            return 0
    else:
        print("bad hgt")
        return 1

def valhcl(string):
    if string.find("#") != -1:
        h = string.lstrip('#')
    if len(h) == 6:
        try:
            int(h, 16)
        except:
            print("bad hcl")
            return 1
        return 0
    else:
        print("bad hcl")
        return 1

def valecl(string):
    colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    for c in colors:
        if string == c:
            return 0
    print("bad ecl")
    return 1

def valpid(string):
    if len(string) == 9 and string.isdigit():
        return 0
    else:
        print("bad pid")
        return 1

def validate(dlist):
    validcount = 0
    for l in dlist:
        print(l)
        i = 0
        try:
            i = i + valbyr(l['byr'])
        except:
            print("no byr")
            i = i +1
        try:
            i = i + valiyr(l['iyr'])
        except:
            print("no iyr")
            i = i +1
        try:
            i = i + valeyr(l['eyr'])
        except:
            print("no eyr")
            i = i +1
        try:
            i = i + valhgt(l['hgt'])
        except:
            print("no hgt")
            i = i +1
        try:
            i = i + valhcl(l['hcl'])
        except:
            print("no hcl")
            i = i +1
        try:
            i = i + valecl(l['ecl'])
        except:
            print("no ecl")
            i = i +1
        try:
            i = i + valpid(l['pid'])
        except:
            print("no pid")
            i = i +1
        print("bad count =", i)
        if i == 0:
            validcount = validcount +1
    return validcount

testclean = cleanlist(fileimp.listimp('d04.2.test.txt'))
testdict = dictlist(testclean)
if validate(testdict) != 4:
    print("Test failed!")
    quit()

clean = cleanlist(fileimp.listimp('d04.input.txt'))
Dict = dictlist(clean)
print("Number of valid passports =", validate(Dict))

# if validate(cleanlist(fileimp.listimp('d04.1.test.txt'))) != 2:
#     print("Test Failed!")
#     quit()
#
# print("valid passports =", validate(cleanlist(fileimp.listimp('d04.input.txt'))))
