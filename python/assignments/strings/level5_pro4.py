#Write a program to find the first  repeated character in a string.
str="sweety"
str1=""
for ch in str:
    if str.count(ch)>1 :
        print("first  repeated character",ch)
        break;
