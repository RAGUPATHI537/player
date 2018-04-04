a=input()
m=0
while(a!=0):
    c=a%10
    m=c**2+m
    a=a/10
print(m)
