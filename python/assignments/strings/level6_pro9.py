sentence="javaygyv python c"
sen=sentence.split()
largest=sen[0]
smallest=sen[0]
for ch in sen:
    if len(largest)<len(ch):
        largest=ch
    if len(smallest)>len(ch):
        smallest=ch    

print(largest) 
print(smallest)       
     