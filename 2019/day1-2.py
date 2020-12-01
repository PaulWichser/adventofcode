import fileimp

def fuelcalc(mass):
    fuel = int(mass/3-2)
    return fuel

if fuelcalc(1969) != 654 or fuelcalc(100756) != 33583:
    print('Fuel calculation failed')
    quit()

masses = fileimp.listimp('day1-1input.txt')
fueltot = 0
for m in masses:
    fuel = fuelcalc(m)
    while fuel > 0:
        fueltot += fuel
        fuel = fuelcalc(fuel)
print ("Fuel required = %i" % fueltot)
