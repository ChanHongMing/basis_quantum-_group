import quickimp
import mono
import genLib
import numpy
class expressionG2:
    def __init__(self,monomiallist):
        deletedArr=[]
        for i in range(len(monomiallist)):
            if i not in deletedArr:
                for j in range(i+1,len(monomiallist)):
                    if monomiallist[i].generator==monomiallist[j].generator:
                        if j not in deletedArr:
                            monomiallist[i]=monomiallist[i]+monomiallist[j]
                            deletedArr.append(j)
                        else:
                            raise ValueError('implement wrong')
        templist=[]
        for i in range(len(monomiallist)):
            if i not in deletedArr:
                numerator=monomiallist[i].numerator
                if not (numerator.max==numerator.min and numerator.coe[0]==0):
                    templist.append(monomiallist[i])
        
        i=0
        while i<len(templist):
            denominator=templist[i].denominator
            numerator=templist[i].numerator
            generator=templist[i].generator.str
            j=0
            while j<len(generator)-1:
                if generator[j]=='f' and generator[j+1]=='k':
                    generator=generator[:j]+'kf'+generator[j+2:]
                    numerator=numerator*quickimp.laurent(2,2,numpy.array([1],dtype=int))
                    if j>0:
                        j-=1
                    else:
                        j=1
                elif generator[j]=='f' and generator[j+1]=='K':
                    generator=generator[:j]+'Kf'+generator[j+2:]
                    numerator=numerator*quickimp.laurent(-3,-3,numpy.array([1],dtype=int))
                    if j>0:
                        j-=1
                    else:
                        j=1
                elif generator[j]=='F' and generator[j+1]=='k':
                    generator=generator[:j]+'kF'+generator[j+2:]
                    numerator=numerator*quickimp.laurent(-3,-3,numpy.array([1],dtype=int))
                    if j>0:
                        j-=1
                    else:
                        j=1
                elif generator[j]=='F' and generator[j+1]=='K':
                    generator=generator[:j]+'KF'+generator[j+2:]
                    numerator=numerator*quickimp.laurent(6,6,numpy.array([1],dtype=int))
                    if j>0:
                        j-=1
                    else:
                        j=1
                elif generator[j]=='k' and generator[j+1]=='K':
                    generator=generator[:j]+'Kk'+generator[j+2:]
                    if j>0:
                        j-=1
                    else:
                        j=1
                elif generator[j]=='k' and generator[j+1]=='E':
                    generator=generator[:j]+'Ek'+generator[j+2:]
                    numerator=numerator*quickimp.laurent(-3,-3,numpy.array([1],dtype=int))
                    if j>0:
                        j-=1
                    else:
                        j=1
                elif generator[j]=='k' and generator[j+1]=='e':
                    generator=generator[:j]+'ek'+generator[j+2:]
                    numerator=numerator*quickimp.laurent(2,2,numpy.array([1],dtype=int))
                    if j>0:
                        j-=1
                    else:
                        j=1
                elif generator[j]=='K' and generator[j+1]=='E':
                    generator=generator[:j]+'EK'+generator[j+2:]
                    numerator=numerator*quickimp.laurent(6,6,numpy.array([1],dtype=int))
                    if j>0:
                        j-=1
                    else:
                        j=1
                elif generator[j]=='K' and generator[j+1]=='e':
                    generator=generator[:j]+'eK'+generator[j+2:]
                    numerator=numerator*quickimp.laurent(-3,-3,numpy.array([1],dtype=int))
                    if j>0:
                        j-=1
                    else:
                        j=1
                elif generator[j]=='f' and generator[j+1]=='E':
                    generator=generator[:j]+'Ef'+generator[j+2:]
                    if j>0:
                        j-=1
                    else:
                        j=1
                elif generator[j]=='F' and generator[j+1]=='e':
                    generator=generator[:j]+'eF'+generator[j+2:]
                    if j>0:
                        j-=1
                    else:
                        j=1
                elif generator[j]=='f' and generator[j+1]=='j':
                    generator=generator[:j]+'jf'+generator[j+2:]
                    numerator=numerator*quickimp.laurent(-2,-2,numpy.array([1],dtype=int))
                    if j>0:
                        j-=1
                    else:
                        j=1
                elif generator[j]=='f' and generator[j+1]=='J':
                    generator=generator[:j]+'Jf'+generator[j+2:]
                    numerator=numerator*quickimp.laurent(3,3,numpy.array([1],dtype=int))
                    if j>0:
                        j-=1
                    else:
                        j=1
                elif generator[j]=='F' and generator[j+1]=='j':
                    generator=generator[:j]+'jF'+generator[j+2:]
                    numerator=numerator*quickimp.laurent(3,3,numpy.array([1],dtype=int))
                    if j>0:
                        j-=1
                    else:
                        j=1
                elif generator[j]=='F' and generator[j+1]=='J':
                    generator=generator[:j]+'JF'+generator[j+2:]
                    numerator=numerator*quickimp.laurent(-6,-6,numpy.array([1],dtype=int))
                    if j>0:
                        j-=1
                    else:
                        j=1
                elif generator[j]=='j' and generator[j+1]=='J':
                    generator=generator[:j]+'Jj'+generator[j+2:]
                    if j>0:
                        j-=1
                    else:
                        j=1
                elif generator[j]=='j' and generator[j+1]=='E':
                    generator=generator[:j]+'Ej'+generator[j+2:]
                    numerator=numerator*quickimp.laurent(3,3,numpy.array([1],dtype=int))
                    if j>0:
                        j-=1
                    else:
                        j=1
                elif generator[j]=='j' and generator[j+1]=='e':
                    generator=generator[:j]+'ej'+generator[j+2:]
                    numerator=numerator*quickimp.laurent(-2,-2,numpy.array([1],dtype=int))
                    if j>0:
                        j-=1
                    else:
                        j=1
                elif generator[j]=='J' and generator[j+1]=='E':
                    generator=generator[:j]+'EJ'+generator[j+2:]
                    numerator=numerator*quickimp.laurent(-6,-6,numpy.array([1],dtype=int))
                    if j>0:
                        j-=1
                    else:
                        j=1
                elif generator[j]=='J' and generator[j+1]=='e':
                    generator=generator[:j]+'eJ'+generator[j+2:]
                    numerator=numerator*quickimp.laurent(3,3,numpy.array([1],dtype=int))
                    if j>0:
                        j-=1
                    else:
                        j=1
                elif generator[j]=='j' and generator[j+1]=='k':
                    generator=generator[:j]+generator[j+2:]
                    if j>0:
                        j-=1
                    else:
                        j=1
                elif generator[j]=='k' and generator[j+1]=='j':
                    generator=generator[:j]+generator[j+2:]
                    if j>0:
                        j-=1
                    else:
                        j=1
                elif generator[j]=='j' and generator[j+1]=='K':
                    generator=generator[:j]+'Kj'+generator[j+2:]
                    if j>0:
                        j-=1
                    else:
                        j=1
                elif generator[j]=='k' and generator[j+1]=='J':
                    generator=generator[:j]+'kJ'+generator[j+2:]
                    if j>0:
                        j-=1
                    else:
                        j=1
                elif generator[j]=='J' and generator[j+1]=='K':
                    generator=generator[:j]+generator[j+2:]
                    if j>0:
                        j-=1
                    else:
                        j=1
                elif generator[j]=='K' and generator[j+1]=='J':
                    generator=generator[:j]+generator[j+2:]
                    if j>0:
                        j-=1
                    else:
                        j=1
                elif generator[j]=='F' and generator[j+1]=='E':
                    generator=generator[:j]+'EF'+generator[j+2:]
                    tempgen=genLib.genClass(generator[:j]+'K'+generator[j+2:])
                    tempde=denominator*quickimp.laurent(3,-3,numpy.array([1,0,0,0,0,0,-1],dtype=int))
                    templist.append(mono.monomial(tempde,numerator,tempgen))
                    tempgen=genLib.genClass(generator[:j]+'J'+generator[j+2:])
                    tempde=denominator*quickimp.laurent(3,-3,numpy.array([-1,0,0,0,0,0,1],dtype=int))
                    templist.append(mono.monomial(tempde,numerator,tempgen))
                    if j>0:
                        j-=1
                    else:
                        j=1
                elif generator[j]=='f' and generator[j+1]=='e':
                    generator=generator[:j]+'ef'+generator[j+2:]
                    tempgen=genLib.genClass(generator[:j]+'k'+generator[j+2:])
                    tempde=denominator*quickimp.laurent(1,-1,numpy.array([1,0,-1],dtype=int))
                    templist.append(mono.monomial(tempde,numerator,tempgen))
                    tempgen=genLib.genClass(generator[:j]+'j'+generator[j+2:])
                    tempde=denominator*quickimp.laurent(1,-1,numpy.array([-1,0,1],dtype=int))
                    templist.append(mono.monomial(tempde,numerator,tempgen))
                    if j>0:
                        j-=1
                    else:
                        j=1
                else:
                    j+=1
            templist[i].numerator=numerator
            templist[i].generator.str=generator
            i+=1
        
        deletedArr=[]
        for i in range(len(templist)):
            if i not in deletedArr:
                for j in range(i+1,len(templist)):
                    if templist[i].generator==templist[j].generator:
                        if j not in deletedArr:
                            templist[i]=templist[i]+templist[j]
                            deletedArr.append(j)
                        else:
                            raise ValueError('implement wrong')
        self.monomiallist=[]
        for i in range(len(templist)):
            if i not in deletedArr:
                numerator=templist[i].numerator
                if not (numerator.max==numerator.min and numerator.coe[0]==0):
                    self.monomiallist.append(templist[i])


    
    def __add__(self, other):
        newmonomiallist=self.monomiallist+other.monomiallist
        return expressionG2(newmonomiallist)

    def __sub__(self, other):
        newmonomiallist=self.monomiallist+[-i for i in other.monomiallist]
        return expressionG2(newmonomiallist)

    def __neg__(self):
        return expressionG2([-i for i in self.monomiallist])

    def __mul__(self, other):
        newmonomiallist=[]
        for i in self.monomiallist:
            for j in other.monomiallist:
                newmonomiallist.append(i*j)
        return expressionG2(newmonomiallist)

    def __str__(self):
        string=''
        for i in self.monomiallist:
            string+=str(i)+'+'
        return string[:-1]

    def sym(self):
        templist=self.monomiallist
        i=0
        while i<len(templist): 
            denominator=templist[i].denominator
            numerator=templist[i].numerator
            generator=templist[i].generator.str
            j=0
            while j<len(generator)-2:
                if generator[j]=='E' and generator[j+1]=='e' and generator[j+2]=='E':
                    generator=generator[:j]+'EEe'+generator[j+3:]
                    denominator=denominator*quickimp.laurent(3,-3,numpy.array([1,0,0,0,0,0,1],dtype=int))
                    tempgen=genLib.genClass(generator[:j]+'eEE'+generator[j+3:])
                    templist.append(mono.monomial(denominator,numerator,tempgen))
                    if j>0:
                        j-=1
                    else:
                        j=1
                else:
                    j+=1
            templist[i].denominator=denominator
            templist[i].generator.str=generator
            i+=1
        deletedArr=[]
        for i in range(len(templist)):
            if i not in deletedArr:
                for j in range(i+1,len(templist)):
                    if templist[i].generator==templist[j].generator:
                        if j not in deletedArr:
                            templist[i]=templist[i]+templist[j]
                            deletedArr.append(j)
                        else:
                            raise ValueError('implement wrong')
        self.monomiallist=[]
        for i in range(len(templist)):
            if i not in deletedArr:
                numerator=templist[i].numerator
                if not (numerator.max==numerator.min and numerator.coe[0]==0):
                    self.monomiallist.append(templist[i])
        return self

    def T1(self):
        newmonomiallist=[]
        for i in range(len(self.monomiallist)):
            denominator=self.monomiallist[i].denominator
            numerator=self.monomiallist[i].numerator
            generator=self.monomiallist[i].generator.str
            j=0
            expmul=[]
            for j in range(len(generator)):
                if j!=0:
                    if generator[j]=='E':
                        expmul.append(expressionG2([mono.monomial.frommaxmincoe(0,0,numpy.array([1],dtype=int),0,0,numpy.array([-1],dtype=int),'KF')]))
                    elif generator[j]=='e':
                        mono1=mono.monomial.frommaxmincoe(0,0,numpy.array([1],dtype=int),0,0,numpy.array([1],dtype=int),'eE')
                        mono2=mono.monomial.frommaxmincoe(0,0,numpy.array([1],dtype=int),3,3,numpy.array([-1],dtype=int),'Ee')
                        expmul.append(expressionG2([mono1,mono2]))
                    else:
                        raise ValueError('implement wrong')
                else:
                    if generator[j]=='E':
                        expmul.append(expressionG2([mono.monomial(denominator,numerator*quickimp.laurent(0,0,numpy.array([-1],dtype=int)),'KF')]))
                    elif generator[j]=='e':
                        mono1=mono.monomial(denominator,numerator,'eE')
                        mono2=mono.monomial(denominator,numerator*quickimp.laurent(3,3,numpy.array([-1],dtype=int)),'Ee')
                        expmul.append(expressionG2([mono1,mono2]))
                    else:
                        raise ValueError('implement wrong')
            for j in range(len(expmul)-1):
                expmul[j+1]=expmul[j]*expmul[j+1]
            newmonomiallist=newmonomiallist+expmul[-1].monomiallist
        return expressionG2(newmonomiallist)

    def T2(self):
        newmonomiallist=[]
        for i in range(len(self.monomiallist)):
            denominator=self.monomiallist[i].denominator
            numerator=self.monomiallist[i].numerator
            generator=self.monomiallist[i].generator.str
            j=0
            expmul=[]
            for j in range(len(generator)):
                if j!=0:
                    if generator[j]=='E':
                        mono1=mono.monomial.frommaxmincoe(3,-3,numpy.array([1,0,2,0,2,0,1],dtype=int),0,0,numpy.array([1],dtype=int),'Eeee')
                        mono2=mono.monomial.frommaxmincoe(1,-1,numpy.array([1,0,1],dtype=int),1,1,numpy.array([-1],dtype=int),'eEee')
                        mono3=mono.monomial.frommaxmincoe(1,-1,numpy.array([1,0,1],dtype=int),2,2,numpy.array([1],dtype=int),'eeEe')
                        mono4=mono.monomial.frommaxmincoe(3,-3,numpy.array([1,0,2,0,2,0,1],dtype=int),3,3,numpy.array([-1],dtype=int),'eeeE')
                        expmul.append(expressionG2([mono1,mono2,mono3,mono4]))
                    elif generator[j]=='e':
                        expmul.append(expressionG2([mono.monomial.frommaxmincoe(0,0,numpy.array([1],dtype=int),0,0,numpy.array([-1],dtype=int),'kf')]))
                    else:
                        raise ValueError('implement wrong')
                else:
                    if generator[j]=='E':
                        mono1=mono.monomial(denominator*quickimp.laurent(3,-3,numpy.array([1,0,2,0,2,0,1],dtype=int)),numerator,'Eeee')
                        mono2=mono.monomial(denominator*quickimp.laurent(1,-1,numpy.array([1,0,1],dtype=int)),numerator*quickimp.laurent(1,1,numpy.array([-1],dtype=int)),'eEee')
                        mono3=mono.monomial(denominator*quickimp.laurent(1,-1,numpy.array([1,0,1],dtype=int)),numerator*quickimp.laurent(2,2,numpy.array([1],dtype=int)),'eeEe')
                        mono4=mono.monomial(denominator*quickimp.laurent(3,-3,numpy.array([1,0,2,0,2,0,1],dtype=int)),numerator*quickimp.laurent(3,3,numpy.array([-1],dtype=int)),'eeeE')
                        expmul.append(expressionG2([mono1,mono2,mono3,mono4]))
                    elif generator[j]=='e':
                        expmul.append(expressionG2([mono.monomial(denominator,numerator*quickimp.laurent(0,0,numpy.array([-1],dtype=int)),'kf')]))
                    else:
                        raise ValueError('implement wrong')
            for j in range(len(expmul)-1):
                expmul[j+1]=expmul[j]*expmul[j+1]
            newmonomiallist=newmonomiallist+expmul[-1].monomiallist
        return expressionG2(newmonomiallist)

if __name__=='__main__':
    e1=mono.monomial.frommaxmincoe(0,0,numpy.array([1],dtype=int),0,0,numpy.array([1],dtype=int),'E')
    e2=mono.monomial.frommaxmincoe(0,0,numpy.array([1],dtype=int),0,0,numpy.array([1],dtype=int),'e')
    b=expressionG2([e2])
    #c=expressionG2([e1])
    #d=e
    
    a=expressionG2([e1])
    T2e1=a.T2()
    T1T2e1=T2e1.T1()
    T2T1T2e1=T1T2e1.T2()
    T1T2T1T2e1=T2T1T2e1.T1()
    T2T1T2T1T2e1=T1T2T1T2e1.T2()


    
    T1e2=b.T1()
    T2T1e2=T1e2.T2()
    T1T2T1e2=T2T1e2.T1()
    T2T1T2T1e2=T1T2T1e2.T2()
    T1T2T1T2T1e2=T2T1T2T1e2.T1()
    '''
    E2E3=T1e2*T1T2e1
    E3E2=T1T2e1*T1e2
    x2=E2E3-E3E2
    
    k=[]
    m=[]
    for i in E2E3.monomiallist:
        k.append(i.generator.str)
    for i in E3E2.monomiallist:
        m.append(i.generator.str)
    for i in m:
        if i in k:
            print(i)
    print("")
    for i in m:
        if not(i in k):
            print(i)
    for i in k:
        if not(i in m):
            print(i)
    print(len(E3E2.monomiallist))
    print(len(x2.monomiallist))
    print(E2E3)
    print(E3E2)
    print("")
    print(x2)
    '''
    print(a)
    print(T1e2)
    print(T1T2e1)

    print(T1T2T1e2)
    print(T1T2T1T2e1)
    print(T1T2T1T2T1e2)
    print("\n")
    print(b)
    print(T2e1)
    print(T2T1e2)
    print(T2T1T2e1)
    print(T2T1T2T1e2)
    print(T2T1T2T1T2e1)
    
    sT1T2e1=T1T2e1.sym()
    print(sT1T2e1)
    sT2T1T2e1=T2T1T2e1.sym()
    print(sT2T1T2e1)
'''
a=['3','4','5']
b=['4','3','5']
print(a==b)
'''
