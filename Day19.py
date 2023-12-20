import re
from collections import namedtuple
with open('input.txt') as fr:
    maps,parts = fr.read().split('\n\n')

node = namedtuple('node','x m a s')
part_list = list()
for l in parts.splitlines():
    part_list.append(node(*(int(c) for c in re.findall('\d+',l))))

workflow = dict()
for l in maps.splitlines():
    cn = l.split('{')[0]
    conds = [tuple(c.split(':')) for c in l.split('{')[-1][:-1].split(',')]
    workflow[cn] = conds

# print(workflow)

def run_workflow(p:node):
    wf = 'in'
    while True:
        # print(f'{wf} -> ',end='')
        if wf == 'A' or wf == 'R': return wf
        conds = workflow[wf]
        for cond in conds:
            if len(cond) == 1:
                wf = cond[0]
                break
            ll,nwf = cond
            if 'x' in ll and '<' in ll:
                if p.x < int(ll[2:]):
                    wf = nwf
                    break
            if 'x' in ll and '>' in ll:
                if p.x > int(ll[2:]):
                    wf = nwf
                    break
            if 'm' in ll and '<' in ll:
                if p.m < int(ll[2:]):
                    wf = nwf
                    break
            if 'm' in ll and '>' in ll:
                if p.m > int(ll[2:]):
                    wf = nwf
                    break
            if 'a' in ll and '<' in ll:
                if p.a < int(ll[2:]):
                    wf = nwf
                    break
            if 'a' in ll and '>' in ll:
                if p.a > int(ll[2:]):
                    wf = nwf
                    break
            if 's' in ll and '<' in ll:
                if p.s < int(ll[2:]):
                    wf = nwf
                    break
            if 's' in ll and '>' in ll:
                if p.s > int(ll[2:]):
                    wf = nwf
                    break

ans = sum(sum(p) for p in part_list if run_workflow(p) == 'A')
print(f'ans1: {ans}')

def sol2():
    state = namedtuple('state','xl xr ml mr al ar sl sr wf')
    q = [state(1,4e3,1,4e3,1,4e3,1,4e3,'in')]
    accepted_list = list()
    rejected_list = list()
    while q:
        xl,xr,ml,mr,al,ar,sl,sr,wf = q.pop(0)
        if wf == 'A': 
            accepted_list.append(state(xl,xr,ml,mr,al,ar,sl,sr,wf))
            continue
        if wf == 'R':
            rejected_list.append(state(xl,xr,ml,mr,al,ar,sl,sr,wf))
            continue
        conds = workflow[wf]
        for cond in conds:
            if len(cond) == 1:
                nwf = cond[0]
                q.append(state(xl,xr,ml,mr,al,ar,sl,sr,nwf))
                break
            eqn,nwf = cond
            num = int(eqn[2:])
            if 'x<' in eqn:
                q.append(state(xl,num-1,ml,mr,al,ar,sl,sr,nwf))
                xl = num
            if 'x>' in eqn:
                q.append(state(num+1,xr,ml,mr,al,ar,sl,sr,nwf))
                xr = num
            if 'm<' in eqn:
                q.append(state(xl,xr,ml,num-1,al,ar,sl,sr,nwf))
                ml = num
            if 'm>' in eqn:
                q.append(state(xl,xr,num+1,mr,al,ar,sl,sr,nwf))
                mr = num
            if 'a<' in eqn:
                q.append(state(xl,xr,ml,mr,al,num-1,sl,sr,nwf))
                al = num
            if 'a>' in eqn:
                q.append(state(xl,xr,ml,mr,num+1,ar,sl,sr,nwf))
                ar = num
            if 's<' in eqn:
                q.append(state(xl,xr,ml,mr,al,ar,sl,num-1,nwf))
                sl = num
            if 's>' in eqn:
                q.append(state(xl,xr,ml,mr,al,ar,num+1,sr,nwf))
                sr = num
    # print(accepted_list)
    # print([s.sr for s in accepted_list])

    ans = sum((s.xr - s.xl + 1)*(s.mr - s.ml + 1)*(s.ar - s.al + 1)*(s.sr - s.sl + 1) for s in accepted_list)
    print(f'ans2: {ans}')



sol2()
        

        


