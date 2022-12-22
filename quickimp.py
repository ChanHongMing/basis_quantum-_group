import numpy
class laurent:
    def __init__(self, max, min, coe):
        if(len(coe)==max-min+1):
            self.max = max
            self.min = min
            self.coe = coe
            self.trim_zeros()
        else:
            raise Exception("The length of coe is not equal to max-min+1")
        
    def __add__(self, other):
        if(self.max>=other.max and self.min<=other.min):
            max=self.max
            min=self.min
            coe=self.coe+numpy.pad(other.coe,(other.min-self.min,self.max-other.max),'constant')
        elif(self.max<other.max and self.min>other.min):
            max=other.max
            min=other.min
            coe=numpy.pad(self.coe,(self.min-other.min,other.max-self.max),'constant')+other.coe
        elif(self.max>=other.max and self.min>other.min):
            max=self.max
            min=other.min
            coe=numpy.pad(self.coe,(self.min-other.min,0),'constant')+numpy.pad(other.coe,(0,self.max-other.max),'constant')
        elif(self.max<other.max and self.min<=other.min):
            max=other.max
            min=self.min
            coe=numpy.pad(self.coe,(0,other.max-self.max),'constant')+numpy.pad(other.coe,(other.min-self.min,0),'constant')
        return laurent(max,min,coe)

    def __sub__(self, other):
        if(self.max>=other.max and self.min<=other.min):
            max=self.max
            min=self.min
            coe=self.coe-numpy.pad(other.coe,(other.min-self.min,self.max-other.max),'constant')
        elif(self.max<other.max and self.min>other.min):
            max=other.max
            min=other.min
            coe=numpy.pad(self.coe,(self.min-other.min,other.max-self.max),'constant')-other.coe
        elif(self.max>=other.max and self.min>other.min):
            max=self.max
            min=other.min
            coe=numpy.pad(self.coe,(self.min-other.min,0),'constant')-numpy.pad(other.coe,(0,self.max-other.max),'constant')
        elif(self.max<other.max and self.min<=other.min):
            max=other.max
            min=self.min
            coe=numpy.pad(self.coe,(0,other.max-self.max),'constant')-numpy.pad(other.coe,(other.min-self.min,0),'constant')
        return laurent(max,min,coe)

    def __neg__(self):
        return laurent(self.max,self.min,-self.coe)

    def __mul__(self, other):
        max=self.max+other.max
        min=self.min+other.min
        coe=numpy.convolve(self.coe,other.coe)
        return laurent(max,min,coe)

    def __eq__(self, other):
        if(self.max==other.max and self.min==other.min):
            return numpy.array_equal(self.coe,other.coe)
        else:
            return False

    def __truediv__(self, other):
        #for(i in range(self.min-other.min,self.max-other.max+1)):
        #    if(self.coe[i+other.min-self.min]%other.coe[i+other.min-self.min]!=0):
        #        raise Exception(f"{other.coe[i+other.min-self.min]} do not divide {self.coe[i+other.min-self.min]}")
        if(self.max-self.min<other.max-other.min):
            raise Exception("The length of the divisor is larger than the dividend")
        resultlen=self.max-self.min-other.max+other.min+1
        a=numpy.zeros(shape=(resultlen,),dtype=int)
        j=0
        for i in range(len(self.coe)):
            if(i<resultlen):
                if(i==0):
                    denom=self.coe[i]
                    fract=denom/other.coe[0]
                    a[i]=fract
                # TODO: calculate coefficient
                elif(i<len(other.coe)):
                    denom=(self.coe[i]-(numpy.flip(a[0:i]).dot(other.coe[1:i+1])))
                    fract=denom/other.coe[0]
                    a[i]=fract
                else:
                    denom=(self.coe[i]-(numpy.flip(a[i-len(other.coe)+1:i]).dot(other.coe[1:])))
                    fract=denom/other.coe[0]
                    a[i]=fract
            else:
                #Todo:handle the case of other.coe is longer than resultlen
                if(i>=len(other.coe)):
                    p=numpy.flip(a[i-len(other.coe)+1:])
                    t=other.coe[i-resultlen+1:]
                    q=self.coe[i]
                    if(p.dot(t)!=q):
                        raise Exception("Do not divide")
                else:
                    p=numpy.flip(a)
                    t=other.coe[i-resultlen+1:i+1]
                    q=self.coe[i]
                    if(p.dot(t)!=q):
                        raise Exception("Do not divide")
                    

        return laurent(self.max-other.max,self.min-other.min,a)
        #for(i in range(self.min-other.min,self.max-other.max+1)):
        #    j=i+other.min-self.min
        #    denom=(self.coe[j]-(numpy.flip(other.coe[1:j+1]).dot(a)))
        #    fract=denom/other.coe[0]
        #    numpy.append(a,fract,dtype=int)

    def __floordiv__(self, other):
        if(self.max-self.min<other.max-other.min):
            raise Exception("The length of the divisor is larger than the dividend")
        resultlen=self.max-self.min-other.max+other.min+1
        #TODO: calculate coefficient
        pass

    def trim_zeros(self):
        k=len(self.coe)
        self.coe=numpy.trim_zeros(self.coe, trim='b')
        self.max-=k-len(self.coe)
        k=len(self.coe)
        if(k!=0):
            self.coe=numpy.trim_zeros(self.coe, trim='f')
            self.min+=k-len(self.coe)
        else:
            self.min=0
            self.max=0
            self.coe=numpy.array([0],dtype=int)

    def __str__(self):
        if(self.max==0 and self.min==0):
            return str(self.coe[0])
        else:
            result=""
            for i in range(self.min,self.max+1):
                if(self.coe[i-self.min]!=0):
                    if(self.coe[i-self.min]>1):
                        if(i==self.min):
                            result+=str(self.coe[i-self.min])+"q^"+str(i)
                        else:
                            result+="+"+str(self.coe[i-self.min])+"q^"+str(i)
                    elif(self.coe[i-self.min]==1):
                        if(i==self.min):
                            result+="q^"+str(i)
                        else:
                            result+="+q^"+str(i)
                    else:
                        result+=str(self.coe[i-self.min])+"q^"+str(i)
            return result

def brac(n):
    a=numpy.empty((2*n-1,),dtype=int)
    a[::2]=1
    a[1::2]=0
    return laurent(n-1,-n+1,a)

def lambda_(b,i):
    if(i>b or i<0 or b<0):
        return laurent(0,0,numpy.array([0],dtype=int))
    elif(i==0):
        return laurent(0,0,numpy.array([1],dtype=int))
    else:
        return laurent(-2*i,-2*i,numpy.array([1],dtype=int))*lambda_(b-1,i)+lambda_(b-1,i-1)

def bracfac(n):
    if(n==0 or n==1):
        return laurent(0,0,numpy.array([1],dtype=int))
    return brac(n)*bracfac(n-1)

def coef_mat(a,b,c,i):
    numerator=laurent(b*i,b*i,numpy.array([1],dtype=int))*lambda_(c,i)
    if(i==0):
        return numerator
    for k in range(1,i+1):
        numerator=numerator*brac(a+k)
    for k in range(1,i+1):
        numerator=numerator/brac(c-k+1)
    return numerator

def coef_exp(a,b,c):
    if(b>=a+c and b>=0 and a>=0 and c>=0):
        s=''
        for i in range(0,c+1):
            s+=str(coef_mat(a,b,c,i))
            s+=f'F_1^({a+i})F_b^({c-i})F_2^({b-c+i})'
            if(i!=c):
                s+='+'
        return s

    
#for b in range(0,10):
#    print(lambda_(b,3))

#print(coef_mat(1,3,2,2))
#print(__version__)
'''for b in range(0,20):
    for a in range(0,b+1):
        for c in range(0,b-a+1):
            print(f"F_1^{a}F_2^{b}F_3^{c}="+coef_exp(a,b,c))'''

if __name__ == "__main__":
    # execute only if run as a script
    print(laurent(5,1,numpy.array([1,4,7,9,1],dtype=int))/laurent(4,0,numpy.array([1,4,7,9,1],dtype=int)))