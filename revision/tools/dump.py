import json, sys
sys.path.insert(0,".")
from edits import EDITS
p=json.load(open("d3_paras.json"))
for eid,cat,idx,old,new,note in EDITS:
    hits=[k for k,t in enumerate(p) if old in t]
    i=idx if (idx<len(p) and old in p[idx]) else (hits[0] if len(hits)==1 else min(hits,key=lambda k:abs(k-idx)))
    p[i]=p[i].replace(old,new)

def bounds(pref):
    s=[k for k,t in enumerate(p) if t.strip().startswith(pref)][0]
    e=len(p)
    for k in range(s+1,len(p)):
        t=p[k].strip()
        if t.startswith(("Chapter ","CUSTOS Interlude","Coda ","Notices","THE END")): e=k; break
    return s,e

def dump(pref, head=6, w_head=1200, w=230):
    s,e=bounds(pref)
    print("#"*10, p[s], f"({e-s-1} paras, {sum(len(x.split()) for x in p[s:e])} words)")
    for k in range(s,e):
        lim = w_head if k-s <= head else w
        print(f"[{k}] {p[k][:lim]}")
    print()
if __name__=="__main__":
    for pref in sys.argv[1:]:
        dump(pref)
