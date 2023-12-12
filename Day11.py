with open('input.txt','r') as fr:
    inp = [[c for c in r if c!='\n'] for r in fr.readlines()]

def day11(inp,empty_space):
    NI,NJ = len(inp),len(inp[0])
    dist = [[1 for _ in range(NJ)] for _ in range(NI)]
    # search row
    for i,r in enumerate(inp):
        if '#' not in r: dist[i] = [empty_space for _ in range(NI)]
    # search column
    for j in range(NJ):
        c = [inp[i][j] for i in range(NI)]
        if '#' not in c:
            for i in range(NI): dist[i][j] = empty_space
    # for r in dist: print(r)
    gs = [(i,j) for i in range(NI) for j in range(NJ) if inp[i][j] == '#']
    # print(gs)
    # (5,1)-(9,4) -> 9
    distance = lambda x1,y1,x2,y2:sum([v[0] for v in dist[x1:x2]]) + sum(dist[0][y1:y2])
    total = 0
    for i in range(len(gs)):
        for j in range(i):
            x1,y1 = gs[i]
            x2,y2 = gs[j]
            if x1 > x2: x1,x2 = x2,x1
            if y1 > y2: y1,y2 = y2,y1
            # print(f'{(x1,y1)}->{(x2,y2)}: {distance(x1,y1,x2,y2)}')
            total += distance(x1,y1,x2,y2)
    return total

print(f'ans1: {day11(inp,2)}')
print(f'ans2: {day11(inp,1000000)}')