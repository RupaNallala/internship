str="java is a programming language"
words = str.split()
smallest = words[0]

for word in words:
    if len(word)<len(largest):
         smallest = word

print("smallest word:", smallest)