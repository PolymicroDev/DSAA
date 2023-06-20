with open("Desktop/GitHub/poem.txt","r") as p:
    for line in p:
        print(line)

words = {}
with open("Desktop/GitHub/poem.txt","r") as p:
    for line in p:
        for word in line.split(" "):
            word = word.replace('\n','')
            if word in words.keys():
                words[word] += 1
                continue
            words[word] = 1

 

print(words)