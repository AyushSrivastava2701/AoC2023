import copy
with open('input.txt','r') as fr:
    inp = fr.readlines()


def check_pallindrom(ll:list):
    N = len(ll)
    for c in range(1,N):
        rl = ll[:c][::-1]
        rr = ll[c:]
        rl = rl[:len(rr)]
        rr = rr[:len(rl)]
        if rr == rl: return c
    return 0


def check_pallindrom2(ll:list):
    N = len(ll)
    for c in range(1,N):
        rl = ll[:c][::-1]
        rr = ll[c:]
        rl = rl[:len(rr)]
        rr = rr[:len(rl)]
        # if rr == rl: return c
        if sum(sum(0 if v1 == v2 else 1 for v1,v2 in zip(r1,r2)) for r1,r2 in zip(rl,rr)) == 1: return c
    return 0


def return_val(mtrx):
    rci = check_pallindrom(mtrx)
    rci2 = check_pallindrom2(mtrx)
    mtrx2 = list(zip(*mtrx))
    cci = check_pallindrom(mtrx2)
    cci2 = check_pallindrom2(mtrx2)
    return rci*100 + cci, rci2*100 + cci2

 
res = 0
res2 = 0
mtrx = list()
for l in inp:
    if '.' in l or '#' in l:
        mtrx.append([c for c in l if c != '\n'])
    else:
        a,b = return_val(mtrx)
        res += a
        res2 += b
        mtrx = list()
a,b = return_val(mtrx)
res += a
res2 += b
print(f'ans1: {res}')
print(f'ans2: {res2}')