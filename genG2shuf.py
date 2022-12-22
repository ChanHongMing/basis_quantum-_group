def equal_list(a,b):
    if(len(a)!=len(b)):
        return False
    for i in range(len(a)):
        if(a[i] not in b):
            return False
    for i in range(len(b)):
        if(b[i] not in a):
            return False
    return True

import numpy
nu=16
a=numpy.zeros((121,201))
for i in range(0,nu):
    for j in range(0,nu):
        for k in range(0,nu):
            for l in range(0,nu):
                for m in range(0,nu):
                    for n in range(0,nu):
                        begin=[0,0]
                        begin[0]+=i
                        begin[0]+=j
                        begin[1]+=j
                        begin[0]+=2*k
                        begin[1]+=3*k
                        begin[0]+=l
                        begin[1]+=2*l
                        begin[0]+=m
                        begin[1]+=3*m
                        begin[1]+=n
                        #if(begin==a):
                            #count+=1
                            #print(i,j,k,l,m,n)
                        a[begin[0],begin[1]]+=1
'''
print(a,count,end=' ')
if(c==7):
    print()
'''
b=a[:nu,:nu]
c=numpy.zeros((nu,nu))
for i in range(1,nu):
    for j in range(0,nu):
        c[i,j]=b[i,j]-b[i-1,j]
print(a[:nu,:nu])
print(c)