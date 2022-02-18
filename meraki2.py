a=open("people-exersise.txt")
b=a.readline()
print(b)
i=0
while i<len(b):
    a.write(b[i])
    a.write("/n")
    i=i+1
print(a)
