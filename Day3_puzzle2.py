from collections import defaultdict


inp = list()
with open('input.txt','r') as fr:
    for l in fr: inp.append([c for c in l[:-1]])

def find_symbol(inp):
    NI,NJ = len(inp),len(inp[0])
    gear_num = 1
    map_ngbr = [[0 for j in range(NJ)] for i in range(NI)]
    for i in range(NI):
        for j in range(NJ):
            if inp[i][j] == '*':
                map_ngbr[i][j] = gear_num
                if i == 0 and j == 0:
                    map_ngbr[i][j+1] = gear_num
                    map_ngbr[i+1][j+1] = gear_num
                    map_ngbr[i+1][j] = gear_num
                elif i == 0 and j == NJ-1:
                    map_ngbr[i][j-1] = gear_num
                    map_ngbr[i+1][j-1] = gear_num
                    map_ngbr[i+1][j] = gear_num
                elif i == NI-1 and j == 0:
                    map_ngbr[i-1][j] = gear_num
                    map_ngbr[i-1][j+1] = gear_num
                    map_ngbr[i][j+1] = gear_num
                elif i == NI-1 and j == NJ-1:
                    map_ngbr[i-1][j] = gear_num
                    map_ngbr[i-1][j-1] = gear_num
                    map_ngbr[i][j-1] = gear_num
                
                elif i == 0 and j > 0 and j < NJ-1:
                    map_ngbr[i][j-1] = gear_num
                    map_ngbr[i][j+1] = gear_num
                    map_ngbr[i+1][j-1] = gear_num
                    map_ngbr[i+1][j] = gear_num
                    map_ngbr[i+1][j+1] = gear_num
                elif i == NI-1 and j > 0 and j < NJ-1:
                    map_ngbr[i][j-1] = gear_num
                    map_ngbr[i][j+1] = gear_num
                    map_ngbr[i-1][j-1] = gear_num
                    map_ngbr[i-1][j] = gear_num
                    map_ngbr[i-1][j+1] = gear_num
                elif i > 0 and i < NI-1 and j == 0:
                    map_ngbr[i-1][j] = gear_num
                    map_ngbr[i-1][j+1] = gear_num
                    map_ngbr[i][j+1] = gear_num
                    map_ngbr[i+1][j+1] = gear_num
                    map_ngbr[i+1][j] = gear_num
                elif i > 0 and i < NI-1 and j == NJ-1:
                    map_ngbr[i-1][j] = gear_num
                    map_ngbr[i-1][j-1] = gear_num
                    map_ngbr[i][j-1] = gear_num
                    map_ngbr[i+1][j-1] = gear_num
                    map_ngbr[i+1][j] = gear_num
                elif i > 0 and i < NI-1 and j > 0 and j < NJ-1:
                    map_ngbr[i-1][j-1],map_ngbr[i-1][j],map_ngbr[i-1][j+1] = gear_num,gear_num,gear_num
                    map_ngbr[i][j-1],map_ngbr[i][j],map_ngbr[i][j+1] =      gear_num,gear_num,gear_num
                    map_ngbr[i+1][j-1],map_ngbr[i+1][j],map_ngbr[i+1][j+1] = gear_num,gear_num,gear_num
                gear_num += 1
    return map_ngbr


def func(inp):
    NI,NJ = len(inp),len(inp[0])
    map_ngbr = find_symbol(inp)
    map_ngbr2 = [[0 for j in range(NJ)] for i in range(NI)]
    # print()
    map_digits = [[inp[i][j].isdigit() and map_ngbr[i][j] for j in range(NJ)] for i in range(NI)]
    # for r in map_digits: print(' '.join('T' if i else 'F' for i in r))
    map_num = list()
    cf = 0
    for i,r in enumerate(inp):
        row = list()
        for j,c in enumerate(r):
            if not c.isdigit():
                row.append(0)
                cf = 0
                continue
            if len(row): row.append(row[-1]*10 + int(c)); row[-2] = 0
            else: row.append(int(c))
            cf = map_ngbr[i][j] or cf
            map_ngbr2[i][j] = cf
        # print(row)
        map_num.append(row)
    # for r in map_ngbr2: print(' '.join(str(i) for i in r))
    gear_ratio = defaultdict(list)
    for i in range(NI):
        for j in range(NJ):
            if map_num[i][j]: gear_ratio[map_ngbr2[i][j]].append(map_num[i][j])
    print(gear_ratio)
    final_dict = {k:v for k,v in gear_ratio.items() if len(v)==2 and k!=0}
    print(final_dict)
    print(sum(v[0]*v[1] for v in final_dict.values()))
    # print(sum(map_num[i][j]*map_ngbr2[i][j] for i in range(NI) for j in range(NJ)))





# Part 1: 413
# Part 2: 6756
func(inp)