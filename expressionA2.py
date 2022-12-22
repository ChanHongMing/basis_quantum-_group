import quickimp
import mono
import genLib
import numpy
class expressionA2:
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
                if generator[j]=='f' and generator[j+1]=='b':
                    generator=generator[:j]+'bf'+generator[j+2:]
                    numerator=numerator*quickimp.laurent(-1,-1,numpy.array([1],dtype=int))
                    if j>0:
                        j-=1
                    else:
                        j=1
                elif generator[j]=='b' and generator[j+1]=='F':
                    generator=generator[:j]+'Fb'+generator[j+2:]
                    numerator=numerator*quickimp.laurent(-1,-1,numpy.array([1],dtype=int))
                    if j>0:
                        j-=1
                    else:
                        j=1
                elif generator[j]=='f' and generator[j+1]=='F':
                    generator=generator[:j]+'Ff'+generator[j+2:]
                    tempgen=genLib.genClass(generator[:j]+'b'+generator[j+2:])
                    templist.append(mono.monomial(denominator,numerator,tempgen))
                    numerator=numerator*quickimp.laurent(1,1,numpy.array([1],dtype=int))
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
        return expressionA2(newmonomiallist)

    def __mul__(self, other):
        newmonomiallist=[]
        for i in self.monomiallist:
            for j in other.monomiallist:
                newmonomiallist.append(i*j)
        return expressionA2(newmonomiallist)

    def __str__(self):
        string=''
        for i in self.monomiallist:
            string+=str(i)+'+'
        return string[:-1]

if __name__=='__main__':
    e1=mono.monomial.frommaxmincoe(0,0,numpy.array([1],dtype=int),0,0,numpy.array([1],dtype=int),'fFfFffFfF')
    b=expressionA2([e1])
    print(b)