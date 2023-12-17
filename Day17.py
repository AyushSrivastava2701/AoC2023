from heapq import heappop, heappush
from collections import namedtuple
with open('input.txt') as fr:
    grid = [[int(c) for c in r] for r in fr.read().splitlines()]
# print(grid)
NI,NJ = len(grid),len(grid[0])
node = namedtuple('node','spr i j di dj c')

min_dist = [[float('inf') for _ in range(NJ)] for _ in range(NI)]
visited = set()

hq = [node(0,0,0,0,0,0)]
while hq:
    n = heappop(hq)
    min_dist[n.i][n.j] = min(min_dist[n.i][n.j],n.spr)
    if n.i == NI-1 and n.j == NJ-1:
        break
    if (n.i,n.j,n.di,n.dj,n.c) in visited: continue
    visited.add((n.i,n.j,n.di,n.dj,n.c))
    # check direction-count; if n.c > 2 -> change direction and continue
    # 3 locations to visit, 1 already visited
    for ndi,ndj in [(0,1),(1,0),(0,-1),(-1,0)]:
        ni = n.i + ndi
        nj = n.j + ndj
        if ni < 0 or ni > NI -1 or nj < 0 or nj > NJ-1: continue
        if (ndi,ndj) == (-n.di,-n.dj): continue
        if (ndi,ndj) == (n.di,n.dj) and n.c < 3:
            heappush(hq,node(n.spr + grid[ni][nj],ni,nj,ndi,ndj,n.c + 1))
        if (ndi,ndj) != (n.di,n.dj):
            heappush(hq,node(n.spr + grid[ni][nj],ni,nj,ndi,ndj,1))


# for r in min_dist: print(' '.join(str(v) for v in r))

print(f'ans1: {min_dist[NI-1][NJ-1]}')


min_dist = [[float('inf') for _ in range(NJ)] for _ in range(NI)]
visited = set()
hq = [node(0,0,0,0,0,0)]
while hq:
    n = heappop(hq)
    min_dist[n.i][n.j] = n.spr
    if n.i == NI-1 and n.j == NJ-1 and n.c >= 4:
        break
    if (n.i,n.j,n.di,n.dj,n.c) in visited: continue
    visited.add((n.i,n.j,n.di,n.dj,n.c))
    # check direction-count; if n.c > 2 -> change direction and continue
    # 3 locations to visit, 1 already visited
    for ndi,ndj in [(0,1),(1,0),(0,-1),(-1,0)]:
        ni = n.i + ndi
        nj = n.j + ndj
        if ni < 0 or ni > NI -1 or nj < 0 or nj > NJ-1: continue
        if (ndi,ndj) == (-n.di,-n.dj): continue
        if (ndi,ndj) == (n.di,n.dj) and n.c < 10:
            heappush(hq,node(n.spr + grid[ni][nj],ni,nj,ndi,ndj,n.c + 1))
        if (ndi,ndj) != (n.di,n.dj):
            if n.c >= 4 or (n.di,n.dj) == (0,0):
                heappush(hq,node(n.spr + grid[ni][nj],ni,nj,ndi,ndj,1))


# for r in min_dist: print(' '.join(str(v) for v in r))

print(f'ans2: {min_dist[NI-1][NJ-1]}')

