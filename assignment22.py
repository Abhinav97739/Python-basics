def wordcount(words):
    spaceletter=""
    wordcount=1
    for i in words:
        if i.isalnum() or i.isspace() or i=="-" or i=="'":
            spaceletter+=i
        for j in spaceletter:
            if j==" ":
                wordcount+=1
        return wordcount
print(wordcount("James bond is 007"))


