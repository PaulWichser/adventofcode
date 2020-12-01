import fileimp

# import data as list
# find pair that adds up to 2020
# multiply pair

def paircalc(intlist):
    for i in range(len(intlist)-1):
        for j in range(i+1,len(intlist)):
            x = intlist[i]
            y = intlist[j]
            #print(i,' ',j)
            if x + y == 2020:
                print('2020 sum found at i=', x, ' j=', y)
                ans = x * y
                return ans
            else:
                pass

testint = paircalc(fileimp.intimp('d1.test.txt'))
#print(testint)
if testint != 514579:
    print('Test failed!')
    quit()

print(paircalc(fileimp.intimp('d1.input.txt')))
