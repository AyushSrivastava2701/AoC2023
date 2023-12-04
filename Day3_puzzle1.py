inp = list()
with open('input.txt','r') as fr:
    for l in fr: inp.append([c for c in l[:-1]])

def find_symbol(inp):
    NI,NJ = len(inp),len(inp[0])
    map_ngbr = [[False for j in range(NJ)] for i in range(NI)]
    for i in range(NI):
        for j in range(NJ):
            if ('.' not in inp[i][j]) and (not inp[i][j].isdigit()):
                map_ngbr[i][j] = True
                if i == 0 and j == 0:
                    map_ngbr[i][j+1] = True
                    map_ngbr[i+1][j+1] = True
                    map_ngbr[i+1][j] = True
                elif i == 0 and j == NJ-1:
                    map_ngbr[i][j-1] = True
                    map_ngbr[i+1][j-1] = True
                    map_ngbr[i+1][j] = True
                elif i == NI-1 and j == 0:
                    map_ngbr[i-1][j] = True
                    map_ngbr[i-1][j+1] = True
                    map_ngbr[i][j+1] = True
                elif i == NI-1 and j == NJ-1:
                    map_ngbr[i-1][j] = True
                    map_ngbr[i-1][j-1] = True
                    map_ngbr[i][j-1] = True
                
                elif i == 0 and j > 0 and j < NJ-1:
                    map_ngbr[i][j-1] = True
                    map_ngbr[i][j+1] = True
                    map_ngbr[i+1][j-1] = True
                    map_ngbr[i+1][j] = True
                    map_ngbr[i+1][j+1] = True
                elif i == NI-1 and j > 0 and j < NJ-1:
                    map_ngbr[i][j-1] = True
                    map_ngbr[i][j+1] = True
                    map_ngbr[i-1][j-1] = True
                    map_ngbr[i-1][j] = True
                    map_ngbr[i-1][j+1] = True
                elif i > 0 and i < NI-1 and j == 0:
                    map_ngbr[i-1][j] = True
                    map_ngbr[i-1][j+1] = True
                    map_ngbr[i][j+1] = True
                    map_ngbr[i+1][j+1] = True
                    map_ngbr[i+1][j] = True
                elif i > 0 and i < NI-1 and j == NJ-1:
                    map_ngbr[i-1][j] = True
                    map_ngbr[i-1][j-1] = True
                    map_ngbr[i][j-1] = True
                    map_ngbr[i+1][j-1] = True
                    map_ngbr[i+1][j] = True
                elif i > 0 and i < NI-1 and j > 0 and j < NJ-1:
                    map_ngbr[i-1][j-1],map_ngbr[i-1][j],map_ngbr[i-1][j+1] = True,True,True
                    map_ngbr[i][j-1],map_ngbr[i][j],map_ngbr[i][j+1] =      True,True,True
                    map_ngbr[i+1][j-1],map_ngbr[i+1][j],map_ngbr[i+1][j+1] = True,True,True
    return map_ngbr


def func(inp):
    NI,NJ = len(inp),len(inp[0])
    map_ngbr = find_symbol(inp)
    # for r in map_ngbr: print(' '.join('T' if i else 'F' for i in r))
    map_ngbr2 = [[False for j in range(NJ)] for i in range(NI)]
    map_digits = [[inp[i][j].isdigit() for j in range(NJ)] for i in range(NI)]
    map_num = list()
    cf = False
    for i,r in enumerate(inp):
        row = list()
        for j,c in enumerate(r):
            if not c.isdigit():
                row.append(0)
                cf = False
                continue
            if len(row): row.append(row[-1]*10 + int(c)); row[-2] = 0
            else: row.append(int(c))
            cf = map_ngbr[i][j] or cf
            map_ngbr2[i][j] = cf
        # print(row)
        map_num.append(row)
    print(sum(map_num[i][j]*map_ngbr2[i][j] for i in range(NI) for j in range(NJ)))





# Part 1: 413
# Part 2: 6756
func(inp)