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

def pattlist(patt,step,inlength):
    list = []
    while len(list) <= inlength:
        for i in patt:
            j = 0
            while j <= step:
                list.append(i)

    list.pop(0)
    return list
