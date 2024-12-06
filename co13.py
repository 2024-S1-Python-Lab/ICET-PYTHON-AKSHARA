s=input("Enter the sentence")
print(s)
wordList=s.split()
print(wordList)
for i in wordList:
    print(f"{i} occures {wordList.count(i)} times")
