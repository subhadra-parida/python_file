# file1=open("FILEQ1.txt")
# file2=file1.read()
# print(file2)
# file1.close()
file1=open("FILEQ1.txt")
file2=file1.readlines()
print(file2)
i=0
count=0
while i<len(file2):
    count=count+1
    i=i+1
print(count)
