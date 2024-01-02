file=open("myfile.txt","r")
count=0
for line in file:
  words=line.split(" ")
  count+=len(words)
  file.close()
  print("number of words in a text file:",count)
