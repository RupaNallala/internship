str="rUpa lAtha"
count1=0
count2=0
for ch in str:
    if ch.isupper():
       count1=count1+1
    if ch.islower(): 
       count2=count2+1
print("uppercase",count1)
print("lowercase",count2)  
