import itertools

def genstr2(n,r):
    listt=[]
    a="E"*n
    for i in itertools.combinations(range(n), r):
        p=list(a)
        for j in i:
            p[j]='e'
        listt.append(''.join(p))
    return listt

def minmonomialbase(nt,rt,numbase):
    listt=genstr2(nt,rt)
    print("All monomial:",listt)
    count=0
    maxlen=numbase
    for tuple in itertools.combinations(listt,numbase):
        newl=[]
        for i in range(numbase):
            newl.append(tuple[i])
        newfl=newl.copy()
        initlen=len(newfl)
        finallen=0
        while finallen!=initlen:
            initlen=finallen
            for m in range(len(newfl)-1):
                for n in range(m+1,len(newfl)):
                    for pos in range(nt-2):
                        if(newfl[m][:pos]==newfl[n][:pos]):
                            if(newfl[m][pos+3:]==newfl[n][pos+3:]):
                                if(newfl[m][pos:pos+3]=='EeE' and newfl[n][pos:pos+3]=='eEE'):
                                    newstr=newfl[m][:pos]+'EEe'+newfl[m][pos+3:]
                                    if(newstr not in newfl):
                                        newfl.append(newstr)
                                elif(newfl[m][pos:pos+3]=='EeE' and newfl[n][pos:pos+3]=='EEe'):
                                    newstr=newfl[m][:pos]+'eEE'+newfl[m][pos+3:]
                                    if(newstr not in newfl):
                                        newfl.append(newstr)
                                elif(newfl[m][pos:pos+3]=='EEe' and newfl[n][pos:pos+3]=='EeE'):
                                    newstr=newfl[m][:pos]+'eEE'+newfl[m][pos+3:]
                                    if(newstr not in newfl):
                                        newfl.append(newstr)
                                elif(newfl[m][pos:pos+3]=='EEe' and newfl[n][pos:pos+3]=='eEE'):
                                    newstr=newfl[m][:pos]+'EeE'+newfl[m][pos+3:]
                                    if(newstr not in newfl):
                                        newfl.append(newstr)
                                elif(newfl[m][pos:pos+3]=='eEE' and newfl[n][pos:pos+3]=='EEe'):
                                    newstr=newfl[m][:pos]+'EeE'+newfl[m][pos+3:]
                                    if(newstr not in newfl):
                                        newfl.append(newstr)
                                elif(newfl[m][pos:pos+3]=='eEE' and newfl[n][pos:pos+3]=='EeE'):
                                    newstr=newfl[m][:pos]+'EEe'+newfl[m][pos+3:]
                                    if(newstr not in newfl):
                                        newfl.append(newstr)
            finallen=len(newfl)
        if(len(newfl)>maxlen):
            maxlen=len(newfl)
            print(newl)
            print(newfl)
            print("maxlen:",maxlen)
        if(len(newfl)==len(listt)):
            if(count==0):
                print("1st Monomial Basis:",newl)
                print("Generates:",newfl)
            count+=1
    return count

p=[]
q=[]
for i in range(3,13):
    p.append(minmonomialbase(i,2,3))
    q.append(minmonomialbase(i,2,4))
print(p)
print(q)