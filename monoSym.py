from sympy.polys.fields import FracField
from sympy import QQ
from sympy import symbols
class monosym:
    def __init__(self,coeff,generator):
        self.generator=generator
        q=symbols('q',commutative=True)
        rf=FracField(symbols=q,domain=QQ)
        if(coeff.field==rf):
            self.coeff=coeff

    def __mul__(self,other):
        coeff=self.coeff*other.coeff
        generator=self.generator+other.generator

if(__name__=="__main__"):
    q=symbols('q',commutative=True)
    rf=FracField(symbols=q,domain=QQ)
    m1=monosym(rf(1/(q+q**(-1))),'E')
    print(m1.coeff)
    print(m1.generator)
