a=[1,2,3,4]
k=0
while k<len(a):
    if k%2==0:
        a.append(k+1)
    print(k)
    k=k+1