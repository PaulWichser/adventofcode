import fileimp

# listimp data as list
# iterate through list of strings, concatenating into larger string
#   if list entry is blank '', end string, start over
# search strings for byr, iyr, eyr, hgt, hcl, ecl, pid, cid (optional)
# if all but cid, valid, iterate count

def cleanlist(list):
    returnlist = []
    string = ""
    for i in list:
        if i == '':
            returnlist.append(string)
            string = ""
        else:
            string = string + " " + i
    return returnlist

def validate(list):
    valid = 0
    for i in list:
        if \
        i.find("byr") != -1 and\
        i.find("iyr") != -1 and\
        i.find("eyr") != -1 and\
        i.find("hgt") != -1 and\
        i.find("hcl") != -1 and\
        i.find("ecl") != -1 and\
        i.find("pid") != -1:
            valid = valid + 1
    return valid

if validate(cleanlist(fileimp.listimp('d04.test.txt'))) != 2:
    print("Test Failed!")
    quit()

print("valid passports =", validate(cleanlist(fileimp.listimp('d04.input.txt'))))
