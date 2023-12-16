with open('input.txt','r') as fr:
    inp = [[c for c in r if c !='\n'] for r in fr.readlines()]


mtrx = list(zip(*inp))
# for r in mtrx: print(''.join(r))

def tilt_north(l:list):
    N =  len(l)
    nl = list()
    for i,cr in enumerate(l):
        if cr == 'O': nl.append(cr)
        if cr == '#':
            while len(nl) < i: nl.append('.')
            nl.append(cr)
    while len(nl) < N: nl.append('.')
    # print(nl)
    return nl

mtrx_nt = list()
for r in mtrx: mtrx_nt.append(tilt_north(r))
# for r in list(zip(*mtrx_nt)): print(''.join(r))

N=  len(inp)
ans = sum((N-i)*r.count('O') for i,r in enumerate(list(zip(*mtrx_nt))))
print(f'ans1: {ans}')

def cycle(mtrx):
    for _ in range(4):
        mtrx = list(zip(*mtrx))
        mtrx = [tilt_north(r) for r in mtrx]
        mtrx = [r[::-1] for r in mtrx]
    return mtrx

cycle_pos = list()
cp = inp
while cp not in cycle_pos:
    cycle_pos.append(copy.deepcopy(cp))
    cp = cycle(cp)
    N= len(cp[0])

first = cycle_pos.index(cp)
# print(first)

sindx = first + (1_000_000_000 - first)%(len(cycle_pos) - first)
cp = cycle_pos[sindx]
ans = sum((N-i)*r.count('O') for i,r in enumerate(cp))
print(f'ans2: {ans}')

# tilt_north([c for c in '...OO....O'])


            

