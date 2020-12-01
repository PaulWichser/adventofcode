import fileimp

# import data as list
# find pair that adds up to 2020
# multiply pair

def tripcalc(intlist):
    for i in range(len(intlist)-2):
        x = intlist[i]

        for j in range(i+1,len(intlist)-1):
            y = intlist[j]

            for k in range(j+1,len(intlist)):
                z = intlist[k]

                if x + y + z == 2020:
                    print('2020 sum found at i=', x, ' j=', y, ' k=', z)
                    ans = x * y *z
                    return ans
                else:
                    pass

testint = tripcalc(fileimp.intimp('d1.test.txt'))
#print(testint)
if testint != 241861950:
    print('Test failed!')
    quit()

print(tripcalc(fileimp.intimp('d1.input.txt')))
