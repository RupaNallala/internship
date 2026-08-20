str="sweety"
str2=str.lower()
count=0
for ch in str:
    if ch  not in "aeiou":
      count=count+1
print("consonants",count)
