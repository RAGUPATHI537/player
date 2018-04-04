a=input()
y=a[::-1]
b=list(str(y))
k=[]
for i in range(0,len(b)):
    if b[i] not in ('a','e','i','o','u'):
        k.append(b[i])
print("".join(k))
