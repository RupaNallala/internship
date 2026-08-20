str="java python"
words=str.split()
rev=""
for ch in words:
    rev+=ch[ : :-1]+" "

print(rev)    
