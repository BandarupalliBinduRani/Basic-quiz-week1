s=input("enter the sentence :\n")
s1=s.split(" ")
word=input("enter the word for which you want to check the occurence:")
count=0
for  i in s1:
    if(i==word):
        count=count+1
        print("occurence of the word you entered is:",count)
