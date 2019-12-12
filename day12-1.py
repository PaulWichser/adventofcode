import fileimp

def moonimp(filename):
    inlist = fileimp.intimp(filename)
    moons = {}
    i = 0
    p = 0
    while i < len(inlist):
        p += 1
        moon1 = 'moon%i-1' % p
        moon2 = 'moon%i-2' % p
        moons.setdefault(moon1,[inlist[i],inlist[i+1],inlist[i+2],0,0,0])
        moons.setdefault(moon2,[inlist[i+3],inlist[i+4],inlist[i+5],0,0,0])
        i += 6
    return moons

def moonpos(moons):
    p = 1
    while p <= (len(moons)/2):
        for i in range(3):
            moons['moon%i-1' % p][i] += moons['moon%i-1' % p][i+3]
            moons['moon%i-2' % p][i] += moons['moon%i-2' % p][i+3]
        p += 1
    print(moons)

def moonvel(moons):
    p = 1
    while p*2 <= len(moons):
        dvelx = moons['moon%i-1' % p][0] - moons['moon%i-2' % p][0]
        dvely = moons['moon%i-1' % p][1] - moons['moon%i-2' % p][1]
        dvelz = moons['moon%i-1' % p][2] - moons['moon%i-2' % p][2]
        moons['moon%i-1' % p][3] -= round(dvelx/abs(dvelx))
        moons['moon%i-1' % p][4] -= round(dvely/abs(dvely))
        moons['moon%i-1' % p][5] -= round(dvelz/abs(dvelz))
        moons['moon%i-2' % p][3] += round(dvelx/abs(dvelx))
        moons['moon%i-2' % p][4] += round(dvely/abs(dvely))
        moons['moon%i-2' % p][5] += round(dvelz/abs(dvelz))
        p+=1
    print(moons)

def moonergy(moons):
    energy = 0
    p = 1
    while p <= (len(moons)/2):
        pot1 = abs(moons['moon%i-1' % p][0]) + abs(moons['moon%i-1' % p][1]) + abs(moons['moon%i-1' % p][2])
        pot2 = abs(moons['moon%i-2' % p][0]) + abs(moons['moon%i-2' % p][1]) + abs(moons['moon%i-2' % p][2])
        kin1 = abs(moons['moon%i-1' % p][3]) + abs(moons['moon%i-1' % p][4]) + abs(moons['moon%i-1' % p][5])
        kin2 = abs(moons['moon%i-2' % p][3]) + abs(moons['moon%i-2' % p][4]) + abs(moons['moon%i-2' % p][5])
        energy += (pot1 * kin1) + (pot2 * kin2)
        p += 1
    print('System energy: %i' % energy)
    return energy

def mooncalc(filename,steps):
    moons = moonimp(filename)
    for i in range(steps):
        print('Step %i' % i)
        print('Calculating velocity...')
        if i == 0:
            p = 1
            while p*2 <= len(moons):
                dvelx = moons['moon%i-1' % p][0] - moons['moon%i-2' % p][0]
                dvely = moons['moon%i-1' % p][1] - moons['moon%i-2' % p][1]
                dvelz = moons['moon%i-1' % p][2] - moons['moon%i-2' % p][2]
                moons['moon%i-1' % p][3] -= dvelx
                moons['moon%i-1' % p][4] -= dvely
                moons['moon%i-1' % p][5] -= dvelz
                moons['moon%i-2' % p][3] += dvelx
                moons['moon%i-2' % p][4] += dvely
                moons['moon%i-2' % p][5] += dvelz
                p+=1
        else:
            moonvel(moons)
        print('Calculating position...')
        moonpos(moons)
        print(moons)
    print('Calculating energy...')
    return moonergy(moons)

if mooncalc('day12-1test1.txt',10) != 179 or mooncalc('day12-1test2.txt',100) != 1940:
    print('Test failed!')
    quit()

mooncalc('day12-1input.txt', 1000)
