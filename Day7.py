from collections import defaultdict
import re
inp = list()
with open('input.txt','r') as fr:
    for l in fr:
        c,b = l.split()
        inp.append((c,int(b)))

# print(inp)
card_rank = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
card_rank.reverse()

def get_bundle_category(cs):
    cn= defaultdict(int)
    for c in cs: cn[c]+=1
    cns = sorted([i for i in cn.values()])
    if len(cns) == 1: return 7*(13**6)
    if len(cns) == 2 and 4 in cns: return 6*(13**6)
    if len(cns) == 2 and 3 in cns: return 5*(13**6)
    if len(cns) == 3 and 3 in cns: return 4*(13**6)
    if len(cns) == 3 and 2 in cns: return 3*(13**6)
    if len(cns) == 4: return 2*(13**6)
    return 1*(13**6)

def get_card_number(cs):
    a = 0
    for i,c in enumerate(cs[::-1]): a += (13**i)*(card_rank.index(c))
    return a

def get_card_rank(cs):
    return get_bundle_category(cs) + get_card_number(cs)


# for i in inp: print(f'{i[0]}->{get_bundle_category(i[0])}')
card_soretd = sorted(inp,key=lambda i: get_card_rank(i[0]))
ans = sum((i+1)*n[1] for i,n in enumerate(card_soretd))
print(f'Puzzle 1: {ans}')

card_rank2 = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2','J']
card_rank2.reverse()

def get_card_rank2(cs):
    max_rank = 0
    for i in card_rank:
        cr = get_bundle_category(re.sub('J',i,cs))
        max_rank = max(cr,max_rank)
    return max_rank + get_card_number(cs)

card_soretd = sorted(inp,key=lambda i: get_card_rank2(i[0]))
ans = sum((i+1)*n[1] for i,n in enumerate(card_soretd))
print(f'Puzzle 2: {ans}')