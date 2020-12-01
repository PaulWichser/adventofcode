import fileimp

def fuelcalc(mass):
    fuel = int(mass/3-2)
    return fuel

if fuelcalc(1969) != 654 or fuelcalc(100756) != 33583:
    print('Fuel calculation failed')
    quit()

masses = fileimp.listimp('day1-1input.txt')
fuel = 0
for m in masses:
    fuel += fuelcalc(m)
print ("Fuel required = %i" % fuel)
