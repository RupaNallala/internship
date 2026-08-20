sentence="python is oop"
dup=""
for ch in sentence:
    if  ch not in dup:
        dup=dup+ch

print(dup)        