from collections import namedtuple
from multiprocessing import Pool

with open('input.txt','r') as fr:
    grid = fr.read().splitlines()
NI,NJ = len(grid),len(grid[0])
# x,y pos
# left to right -> (0,1)
# right to left -> (0,-1)
# downward -> (1,0)
# upward -> (-1,0)
# beam ray tuple-> (curr_pos,next_change)
beam = namedtuple('beam','i j ci cj') # i pos, j pos, change i (-1,0,1), change j (-1,0,1)
def sol1(start_pos = beam(0,0,0,1)):
    q = [start_pos]
    visited = [[0 for _ in range(NJ)] for _ in range(NI)]
    visited_beam = set()
    while q:
        b = q.pop()
        # print(b)
        if b.i < 0 or b.i == NI: continue
        if b.j < 0 or b.j == NJ: continue
        if b in visited_beam: continue
        visited[b.i][b.j] += 1
        visited_beam.add(b)
        if grid[b.i][b.j] == '.': q.append(beam(b.i + b.ci,b.j + b.cj,b.ci,b.cj))
        if grid[b.i][b.j] == '-' and b.ci == 0: q.append(beam(b.i + b.ci,b.j + b.cj,b.ci,b.cj))
        if grid[b.i][b.j] == '|' and b.cj == 0: q.append(beam(b.i + b.ci,b.j + b.cj,b.ci,b.cj))

        if grid[b.i][b.j] == '/': 
            q.append(beam(b.i - b.cj,b.j - b.ci,-b.cj,-b.ci))
            # print('found /')
        if grid[b.i][b.j] == '\\': 
            q.append(beam(b.i + b.cj,b.j + b.ci,b.cj,b.ci))
            # print('found \\')

        if grid[b.i][b.j] == '|' and b.cj != 0:
            q.append(beam(b.i-1,b.j,-1,0))
            q.append(beam(b.i+1,b.j,1,0))
        if grid[b.i][b.j] == '-' and b.ci != 0:
            # print('found -')
            q.append(beam(b.i,b.j-1,0,-1))
            q.append(beam(b.i,b.j+1,0,1))
    
    # for r in visited: print(''.join('#' if v else '.' for v in r))
    return sum(sum(1 if v else 0 for v in r) for r in visited)
print(f'ans1: {sol1()}')

def sol2():
    start_pos = list()
    start_pos.extend([beam(0,j,1,0) for j in range(NJ)]) #top
    start_pos.extend([beam(NI-1,j,-1,0) for j in range(NJ)]) #bottom
    start_pos.extend([beam(i,0,0,1) for i in range(NI)]) #left
    start_pos.extend([beam(i,NJ-1,0,-1) for i in range(NI)]) #right
    max_en = 0
    for sp in start_pos:
        en = sol1(sp)
        # print(f'{sp} -> {en}')
        max_en = max(max_en,en)
    # with Pool(len(start_pos)) as p:
    #     en_vals = p.map(sol1,start_pos)
    # max_en = max(en_vals)
    # print(len(start_pos))
    # print(len(en_vals))
    return max_en

print(f'ans2: {sol2()}')
