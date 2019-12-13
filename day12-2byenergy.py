import fileimp
import hashlib
import time

def moonimp(filename):
    inlist = fileimp.intimp(filename)
    moons = {}
    i = 0
    m = 0
    while i < len(inlist):
        moons.setdefault('moon%i' % m,[inlist[i],inlist[i+1],inlist[i+2],0,0,0])
        m += 1
        i += 3
    return moons

def moonpos(moons):

    for m in range(len(moons)):
        for i in range(3):
            moons['moon%i' % m][i] += moons['moon%i' % m][i+3]
    # print(moons)

def moonvel(moons):
    for m in range(len(moons)):
        n = m+1
        while n < len(moons):
            dvelx = moons['moon%i' % m][0] - moons['moon%i' % n][0]
            dvely = moons['moon%i' % m][1] - moons['moon%i' % n][1]
            dvelz = moons['moon%i' % m][2] - moons['moon%i' % n][2]
            if dvelx != 0:
                moons['moon%i' % m][3] -= round(dvelx/abs(dvelx))
                moons['moon%i' % n][3] += round(dvelx/abs(dvelx))
            if dvely != 0:
                moons['moon%i' % m][4] -= round(dvely/abs(dvely))
                moons['moon%i' % n][4] += round(dvely/abs(dvely))
            if dvelz != 0:
                moons['moon%i' % m][5] -= round(dvelz/abs(dvelz))
                moons['moon%i' % n][5] += round(dvelz/abs(dvelz))
            n += 1
    # print(moons)

def moonergy(moons):
    energy = 0
    for m in range(len(moons)):
        pot1 = abs(moons['moon%i' % m][0]) + abs(moons['moon%i' % m][1]) + abs(moons['moon%i' % m][2])
        kin1 = abs(moons['moon%i' % m][3]) + abs(moons['moon%i' % m][4]) + abs(moons['moon%i' % m][5])
        energy += (pot1 * kin1)
    # print('System energy: %i' % energy)
    return energy

def mooncalc(filename,steps):
    moons = moonimp(filename)
    for i in range(steps):
        # print('Step %i' % i)
        # print('Calculating velocity...')
        moonvel(moons)
        # print('Calculating position...')
        moonpos(moons)
        # print(moons)
    print('Calculating energy...')
    return moonergy(moons)

def moonreturn(filename):
    moons = moonimp(filename)
    steps = 0
    energy = str(moonergy(moons))
    states = {energy:[]}
    win = 0
    while win == 0:
        for i in range(len(states[energy])):
            if states[energy][i] == str(moons):
                print('Found it! It took %i steps to repeat a position' % steps)
                win = 1
        states[energy].append(str(moons))
        moonvel(moons)
        moonpos(moons)
        steps += 1
    # hash = hashlib.md5(str(moons).encode('utf-8')).hexdigest()[8:]
    # hashes = []
    # while hash not in hashes:
    #     hashes.append(hash)
    #     moonvel(moons)
    #     moonpos(moons)
    #     hash = hashlib.md5(str(moons).encode('utf-8')).hexdigest()[8:]
    #     # print(hash)
    #     # print(hashes)
    # print('It took %i steps to return the system to repeat a position' % (len(hashes)))


if mooncalc('day12-1test1.txt',10) != 179 or mooncalc('day12-1test2.txt',100) != 1940 or mooncalc('day12-1input.txt', 1000) != 9441:
    print('Test failed!')
    quit()

t = time.time()
print('%i seconds' % (time.time()-t))
moonreturn('day12-1input.txt')
print('%i seconds' % (time.time()-t))
