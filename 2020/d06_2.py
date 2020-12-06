import fileimp
import string

# import file as list, clean list
# for each list item, scrub through string, noting unique answers
#   string.find() != -1
#   groupanslist = 0 list of len(findlist)
#   answers = list of individual answers per group
#   if findlist[x] exists in answers[i], increment groupanslist[x]
#   if groupanslist[x] = len(answers), increment group total

def groupagrees(stringlist,findlist):
    total = 0
    for i in stringlist:
        groupanslist = [0] * len(findlist)
        answers = i.split()
        for j in answers:
            for k in range(len(findlist)):
                if j.find(findlist[k]) != -1:
                    groupanslist[k] = groupanslist[k] + 1
        for j in groupanslist:
            if j == len(answers):
                total = total + 1
    print(total)
    return total

testlist = fileimp.cleanlist(fileimp.listimp('d06_test.txt'))
if groupagrees(testlist,list(string.ascii_lowercase)) != 6:
    print("Test Failed!")
    quit()

grouplist = fileimp.cleanlist(fileimp.listimp('d06_input.txt'))
total = groupagrees(grouplist,list(string.ascii_lowercase))
print("Total added of agreed per group =", total)
