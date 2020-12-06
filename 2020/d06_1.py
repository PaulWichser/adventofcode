import fileimp
import string

# import file as list, clean list
# for each list item, scrub through string, noting unique answers
#   string.find() != -1
# add uniques from each string to total

def groupuniques(stringlist,findlist):
    total = 0
    for i in stringlist:
        group = 0
        for j in findlist:
            if i.find(j) != -1:
                group = group + 1
        total = total + group
    print(total)
    return total

testlist = fileimp.cleanlist(fileimp.listimp('d06_test.txt'))
if groupuniques(testlist,list(string.ascii_lowercase)) != 11:
    print("Test Failed!")
    quit()

grouplist = fileimp.cleanlist(fileimp.listimp('d06_input.txt'))
total = groupuniques(grouplist,list(string.ascii_lowercase))
print("Total added by groups =", total)
