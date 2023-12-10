with open('input.txt','r') as fr:
    inp = fr.readlines()
arrs = [[int(j) for j in l.split()] for l in inp]

def check(arr):
    for i in arr:
        if i!= 0: return True
    return False

def find_next_num(arr):
    diffs = [arr]
    while check(diffs[-1]): 
        diffs.append([diffs[-1][i] - diffs[-1][i-1] for i in range(1,len(diffs[-1]))])
    # part 1
    ans1 = sum(r[-1] for r in diffs)
    ans2 = 0
    while diffs:
        cn = diffs.pop()
        ans2 = cn[0] - ans2
    return ans1,ans2


ans1,ans2 = 0,0
for a in arrs: 
    s1,s2 = find_next_num(a)
    ans1 += s1; ans2 += s2

print(f'ans1: {ans1}, ans2: {ans2}')