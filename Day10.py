from collections import defaultdict
with open('input.txt','r') as fr:
    inp = fr.readlines()
maze = [[c for c in l if c != '\n'] for l in inp]
# print(maze)
# - -> W E
# | -> N S
# L -> N E
# J -> N W
# 7 -> S W
# F -> S E
mc = defaultdict(list)
NI,NJ = len(maze),len(maze[0])
start_pos = None

def check_north(i,j):
    if i==0: return
    if maze[i-1][j] in ['|','7','F','S']: return (i-1,j)
def check_south(i,j):
    if i == NI-1: return
    if maze[i+1][j] in ['|','L','J','S']: return (i+1,j)
def check_east(i,j):
    if j == NJ-1: return
    if maze[i][j+1] in ['-','J','7','S']: return (i,j+1)
def check_west(i,j):
    if j==0: return
    if maze[i][j-1] in ['-','F','L','S']: return (i,j-1)


for i in range(NI):
    for j in range(NJ):
        if maze[i][j] == 'S': start_pos = (i,j)
        if maze[i][j] == '-':
            if check_east(i,j): mc[(i,j)].append(check_east(i,j))
            if check_west(i,j): mc[(i,j)].append(check_west(i,j))
        if maze[i][j] == '|':
            if check_north(i,j): mc[(i,j)].append(check_north(i,j))
            if check_south(i,j): mc[(i,j)].append(check_south(i,j))
        if maze[i][j] == 'L':
            if check_north(i,j): mc[(i,j)].append(check_north(i,j))
            if check_east(i,j): mc[(i,j)].append(check_east(i,j))
        if maze[i][j] == 'J':
            if check_north(i,j): mc[(i,j)].append(check_north(i,j))
            if check_west(i,j): mc[(i,j)].append(check_west(i,j))
        if maze[i][j] == '7':
            if check_south(i,j): mc[(i,j)].append(check_south(i,j))
            if check_west(i,j): mc[(i,j)].append(check_west(i,j))
        if maze[i][j] == 'F':
            if check_south(i,j): mc[(i,j)].append(check_south(i,j))
            if check_east(i,j): mc[(i,j)].append(check_east(i,j))

si,sj = start_pos
for i in range(max(0,si-1),min(NI,si+2)):
    for j in range(max(0,sj-1),min(NJ,sj+2)):
        if start_pos in mc[(i,j)]:mc[start_pos].append((i,j))

# using BFS to find farthest point
visited = set()
distance = defaultdict(int)
distance[start_pos] = 0
q = [start_pos]
cn = start_pos
while q:
    cn = q.pop(0)
    visited.add(cn)
    for c in mc[cn]:
        if c in visited: continue
        visited.add(c)
        q.append(c)
        distance[c] = distance[cn] + 1

            
# for i in range(NI):
#     for j in range(NJ):
#         print(distance[(i,j)],end=' ')
#     print()

print(f'ans1: {max(v for v in distance.values())}')

# using DFS to find close loop
visited = set()
vm = [[False for _ in range(NJ)] for _ in range(NI)]
q = [start_pos]
cn = start_pos
border = list()
while q:
    cn = q.pop()
    border.append(cn)
    visited.add(cn)
    vm[cn[0]][cn[1]]=True
    for c in mc[cn]:
        if c in visited: continue
        visited.add(c)
        q.append(c)
        vm[c[0]][c[1]]=True

# for i in range(NI):
#     for j in range(NJ):
#         print('#' if vm[i][j] else '.',end=' ')
#     print()


# print(border)
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

inside_tile = 0
border_filter = [b for b in border if maze[b[0]][b[1]] not in ['-','|']]
polygon = Polygon(border_filter)
for i in range(NI):
    for j in range(NJ):
        inside_tile += polygon.contains(Point(i,j))
        # print('#' if polygon.contains(Point(i,j)) else '.',end=' ')
    # print()
print(f'ans2: {inside_tile}')