from math import gcd
map = dict()
with open('input.txt','r') as fr:
    nav = [0 if i=='L' else 1 for i in fr.readline()[:-1]]
    N = len(nav)
    _=fr.readline()
    for l in fr:
        pn,_,lc,rc = l.split()
        lc = lc[1:-1]; rc = rc[:-1]
        map[pn] = (lc,rc)
# print(nav)
# print(map)

def get_steps(cn,map):
    steps = 0
    vn = list()
    while cn[-1] != 'Z':
        vn.append(cn)
        dir = nav[steps%N]
        steps += 1
        cn = map[cn][dir]
    return steps

sns = [k for k in map.keys() if k[-1]=='A']
steps = [get_steps(sn,map) for sn in sns]
# print(steps)
lcm= 1
for s in steps:
    lcm = lcm*s//gcd(lcm,s)
print(lcm)