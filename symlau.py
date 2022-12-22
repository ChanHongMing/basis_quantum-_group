from sympy import Poly
from sympy.abc import x
from sympy import polys
import quickimp
import numpy

def symplify(a,b):
    if(len(a.coe)==1 and a.coe[0]==0):
        return quickimp.laurent(0,0,numpy.array([0],dtype=int)),quickimp.laurent(0,0,numpy.array([1],dtype=int))
    lista=numpy.flip(a.coe)
    listb=numpy.flip(b.coe)
    mina=a.min
    minb=b.min
    maxa=a.max
    maxb=b.max
    polya=Poly(lista,x,domain='ZZ')
    polyb=Poly(listb,x,domain='ZZ')
    gcd = polys.polytools.gcd(polya,polyb)
    degminus=gcd.degree()
    resa=polys.polytools.exquo(polya,gcd).all_coeffs()
    resb=polys.polytools.exquo(polyb,gcd).all_coeffs()
    numa=numpy.array(resa,dtype=int)
    numb=numpy.array(resb,dtype=int)
    numa=numpy.flip(numa)
    numb=numpy.flip(numb)
    if (mina==minb):
        return quickimp.laurent(maxa-degminus-mina,0,numa),quickimp.laurent(maxb-degminus-minb,0,numb)
    elif (mina>minb):
        return quickimp.laurent(maxa-degminus-minb,mina-minb,numa),quickimp.laurent(maxb-degminus-minb,0,numb)
    else:
        return quickimp.laurent(maxa-degminus-mina,0,numa),quickimp.laurent(maxb-degminus-mina,minb-mina,numb)


