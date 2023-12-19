import numpy as np
from multiprocessing import Pool
with open('input.txt') as fr:
    inp = [r.split() for r in fr.read().splitlines()]
dir_map = {
    'R':(0,1),
    'L':(0,-1),
    'U':(-1,0),
    'D':(1,0)
}

dirs = [(dir_map[l[0]],int(l[1]),l[2]) for l in inp]
# print(dirs)
TLi,TLj = float('inf'),float('inf')
BRi,BRj = 0,0
border = [(0,0)]
for dir in dirs:
    cx,cy = border[-1]
    # for i in range(1,dir[1]+1):
    nx = cx + dir[0][0]*dir[1]
    ny = cy + dir[0][1]*dir[1]
    border.append((nx,ny))
    BRi = max(nx,BRi)
    BRj = max(ny,BRj)
    TLi = min(nx,TLi)
    TLj = min(ny,TLj)


# print(BRi + 1 - TLi,BRj + 1 - TLj)
# for i in range(TLi,BRi+1):
#     for j in range(TLj,BRj+1):
#         if (i,j) in border: print('#',end='')
#         else: print('.',end='')
#     print()


from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

polygon = Polygon(border)
print(f'ans1: {(2*polygon.area - polygon.length + 2)//2 + polygon.length}')

# print(polygon.area)

# x = [i[0] for i in border]
# y = [i[1] for i in border]
# def PolyArea(x,y):
#     return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))
# print(PolyArea(x,y))

# vals = [[0 for _ in range(TLj,BRj+1)] for _ in range(TLi,BRi+1)]
# for i in range(TLi,BRi+1):
#     for j in range(TLj,BRj+1):
#         if (i,j) in border: vals[i][j] = 1
#         elif polygon.contains(Point(i,j)): vals[i][j] = 1

# ans = sum(vals[i][j] for i in range(TLi,BRi+1) for j in range(TLj,BRj+1))
# print(ans)


def inside_poly(coords:list):
    inside = 0
    for c in coords:
        if c in border:
            inside += 1
            continue
        if polygon.contains(Point(c[0],c[1])): inside += 1
    return inside

# coords = [(i,j) for i in range(TLi,BRi+1) for j in range(TLj,BRj+1)]
# coords_chunk = list()
# for i in range(0,len(coords)+1000,1000):
#     coords_chunk.append(coords[i:i+1000])

# with Pool(len(coords_chunk)) as p:
#     fvals = p.map(inside_poly,coords_chunk)

# print(f'ans1: {sum(fvals)}')

# for r in vals: print(''.join(str(v) for v in r))
dir_map = {
    '0':(0,1),
    '2':(0,-1),
    '3':(-1,0),
    '1':(1,0)
}

dirs = [(dir_map[l[-1][-2]],int(l[-1][2:-2],16)) for l in inp]

TLi,TLj = float('inf'),float('inf')
BRi,BRj = 0,0
border = [(0,0)]
for dir in dirs:
    cx,cy = border[-1]
    # for i in range(1,dir[1]+1):
    nx = cx + dir[0][0]*dir[1]
    ny = cy + dir[0][1]*dir[1]
    border.append((nx,ny))
    BRi = max(nx,BRi)
    BRj = max(ny,BRj)
    TLi = min(nx,TLi)
    TLj = min(ny,TLj)


# print(BRi + 1 - TLi,BRj + 1 - TLj)

polygon = Polygon(border)
print(f'ans2: {(2*polygon.area - polygon.length + 2)//2 + polygon.length}')

# coords = [(i,j) for i in range(TLi,BRi+1) for j in range(TLj,BRj+1)]
# coords_chunk = list()
# for i in range(0,len(coords)+10000,10000):
#     coords_chunk.append(coords[i:i+10000])

# with Pool(len(coords_chunk)) as p:
#     fvals = p.map(inside_poly,coords_chunk)

# print(f'ans2: {sum(fvals)}')