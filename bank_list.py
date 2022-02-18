Bank_lists=["kotak","HDFC","RBL","SBI","Bank Of Baroda"]
file=open("Bank_list.txt","w")
i=0
while i<len("Bank_list.txt"):
    file.write(file[i])
    file.write("/n")
    i=i+1
print(file)


