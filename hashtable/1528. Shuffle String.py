#1528. Shuffle String

def restoreString(s, indices):
    ht = {}
    for st, idx in zip(s, indices):
        ht[idx] = st
    print(ht)
    return "".join([ht[i] for i in sorted(ht)])

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]

print(restoreString(s, indices))