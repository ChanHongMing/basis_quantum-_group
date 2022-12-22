import quickimp
from genLib import genClass
import numpy
from symlau import symplify
class monomial:
    def __init__(self,denominator,numerator,generator):
        self.denominator = denominator
        self.numerator =numerator
        if isinstance(generator,genClass):
            self.generator = generator
        elif isinstance(generator,str):
            self.generator = genClass(generator)
        try:
            #tempnum=self.numerator/self.denominator
            tempnum,tempdenom=symplify(self.numerator,self.denominator)
        except Exception as e:
            for i in e.args:
                if(i=="The length of the divisor is larger than the dividend" or i=="Do not divide"):
                    pass
                else:
                    print(e.args)
        else:
            self.numerator=tempnum
            #self.denominator=quickimp.laurent(0,0,numpy.array([1],dtype=int))
            self.denominator=tempdenom


    @classmethod
    def frommaxmincoe(cls,max1,min1,coe1,max2,min2,coe2,str):
        denominator=quickimp.laurent(max1,min1,coe1)
        numerator=quickimp.laurent(max2,min2,coe2)
        generator=genClass(str)
        return cls(denominator,numerator,generator)

    def __mul__(self, other):
        denominator=self.denominator*other.denominator
        numerator=self.numerator*other.numerator
        newgenerator=self.generator*other.generator
        return monomial(denominator,numerator,newgenerator)

    def __eq__(self, other):
        return self.denominator==other.denominator and self.numerator==other.numerator and self.generator==other.generator

    def __add__(self, other):
        if self.generator==other.generator:
            if(self.denominator==other.denominator):
                return monomial(self.denominator,self.numerator+other.numerator,self.generator)
            else:
                denominator=self.denominator*other.denominator
                numerator=self.numerator*other.denominator+other.numerator*self.denominator
                return monomial(denominator,numerator,self.generator)
        else:
            raise ValueError('The two monomials do not have the same generator.')

    def __sub__(self, other):
        if self.generator==other.generator:
            if(self.denominator==other.denominator):
                return monomial(self.denominator,self.numerator-other.numerator,self.generator)
            else:
                denominator=self.denominator*other.denominator
                numerator=self.numerator*other.denominator-other.numerator*self.denominator
                return monomial(denominator,numerator,self.generator)
        else:
            raise ValueError('The two monomials do not have the same generator.')

    def __neg__(self):
        return monomial(self.denominator,-self.numerator,self.generator)

    def __str__(self) -> str:
        return str(self.numerator)+'/('+str(self.denominator)+')'+str(self.generator)

if __name__=='__main__':
    m1=monomial.frommaxmincoe(0,0,[1],1,0,[1,1],'E')
    m2=monomial.frommaxmincoe(0,0,[1],1,0,[1,1],'f')
    print(m1==m2)
    print(m1*m2)
    print(m2*m1)
    m3=monomial.frommaxmincoe(0,0,[1],1,0,[1,1],'E')
    print(m1==m3)
    m4=monomial.frommaxmincoe(1,0,[1,1],1,-3,[1,4,7,5,2],'E_1^2')
    m5=monomial.frommaxmincoe(1,0,[1,1],1,0,[1,1],'E_2^2')
    print(m5)