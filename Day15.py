from collections import defaultdict
def get_num(ll:str):
    ans = 0
    for c in ll:
        ans += ord(c)
        ans = ans*17
        ans = ans%256
    return ans

with open('input.txt','r') as fr:
    inp = [r.split(',') for r in fr.read().splitlines()]

ans = sum(sum(get_num(v) for v in r) for r in inp)
print(f'ans1: {ans}')

boxes = defaultdict(list)
commands = inp[0]
for step in commands:
    if '=' in step:
        label = step.split('=')[0]
        focal_length  = int(step.split('=')[-1])
        box_no = get_num(label)
        if label not in [v[0] for v in boxes[box_no]]: boxes[box_no].append((label,focal_length))
        else:
            idx = [v[0] for v in boxes[box_no]].index(label)
            boxes[box_no][idx] = (label,focal_length)
    if '-' in step:
        label = step.split('-')[0]
        box_no = get_num(label)
        if label in [v[0] for v in boxes[box_no]]:
            idx = [v[0] for v in boxes[box_no]].index(label)
            _=boxes[box_no].pop(idx)

# print(boxes)
ans = sum((k+1)*sum((i+1)*f[1] for i,f in enumerate(v)) for k,v in boxes.items())
print(f'ans2: {ans}')
