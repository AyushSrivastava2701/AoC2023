# Puzzle2
def return_digit_left(l:str):
    digits = {
        1:[c for c in 'one'],
        2:[c for c in 'two'],
        3:[c for c in 'three'],
        4:[c for c in 'four'],
        5:[c for c in 'five'],
        6:[c for c in 'six'],
        7:[c for c in 'seven'],
        8:[c for c in 'eight'],
        9:[c for c in 'nine'],
    }
    for c in l:
        if c.isdigit(): return int(c)
        for i in range(1,10): 
            if c == digits[i][0]: digits[i].pop(0)
        for i in range(1,10):
            if not len(digits[i]): return i

def return_digit_right(l:str):
    digits = {
        1:[c for c in 'one'],
        2:[c for c in 'two'],
        3:[c for c in 'three'],
        4:[c for c in 'four'],
        5:[c for c in 'five'],
        6:[c for c in 'six'],
        7:[c for c in 'seven'],
        8:[c for c in 'eight'],
        9:[c for c in 'nine'],
    }
    for c in l[::-1]:
        if c.isdigit(): return int(c)
        for i in range(1,10):
            if c == digits[i][-1]: digits[i].pop()
        for i in range(1,10):
            if not len(digits[i]): return i

inp = list()
res = 0
with open('input.txt','r') as fr:
    for l in fr:
        nl = return_digit_left(l)
        nr = return_digit_right(l)
        res += nl*10 + nr
        print(f'{l} -> {nl*10 + nr}')

print(res)

# Puzzle1
# def get_num(l:str):
#     nl,nr=0,0
#     for c in l:
#         if c.isdigit():
#             nl = int(c)
#             break
#     for c in l[::-1]:
#         if c.isdigit():
#             nr = int(c)
#             break
#     print(f'{l[:-1]}->{nl*10 + nr}')
#     return nl*10 + nr
# res = 0
# with open('input.txt','r') as fr:
#     for l in fr:
#         res += get_num(l)
# print(res)