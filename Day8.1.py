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

steps = 0
cn = 'AAA'
vn = list()
while cn != 'ZZZ':
    vn.append(cn)
    dir = nav[steps%N]
    steps += 1
    cn = map[cn][dir]
    # print(cn)

print(steps)