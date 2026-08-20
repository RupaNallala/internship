str="rupavathiii"
str2=str[0]
for ch in str:
    if str.count(ch)>str.count(str2):
        str2=ch
print("most frequent character is:",str2)