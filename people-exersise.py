a=open("people-exersise.txt")
b=a.readline()
print(b)
i=0
count=0
while i<len(b):
    count=count+1
    i=i+1
print(count)
a.close()