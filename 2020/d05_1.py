import fileimp

# divide rows 0-127
#   F = lower half
#   B = upper half
# divide columns 0-7
#   R = upper half
#   L = lower half
# seat ID = row * 8 + col
# list of IDs
# max list

def idcalc(list):
    seats = []
    for i in list:
        row = ''
        col = ''
        for j in i:
            if j == 'F':
                row = row + '0'
            elif j == 'B':
                row = row + '1'
            elif j == 'R':
                col = col + '1'
            elif j == 'L':
                col = col + '0'
            else:
                print("something went wrong in rows & cols")
                quit()
        print(row, col)
        # row = row[::-1]
        # col = col[::-1]
        print(row, col)
        row = int(row, 2)
        col = int(col, 2)
        print(row, col)
        seats.append((row * 8) + col)
    print(seats)
    return seats

testlist = fileimp.listimp("d05_test.txt")
if max(idcalc(testlist)) != 820:
    print("Test Failed!")
    quit()

seatlist = fileimp.listimp("d05_input.txt")
print("Largest seat ID = ", max(idcalc(seatlist)))
