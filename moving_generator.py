class generator_experssion:
    def __init__(self,expr):
        self.expr=expr

    def SimplifyToMonomial(self):
        temp=self.expr
        tempmono=temp.split('+')
        mono=[]
        for i in tempmono:
            strr=i.split('-')
            if(strr[0]==''):
                strr.pop(0)
                for j in strr:
                    mono.append('-'+j)
            else:
                mono.append(strr[0])
                strr.pop(0)
                for j in strr:
                    mono.append('-'+j)
        '''base=temp.split('E_')
        print(base)
        base=base[1:]
        basepow=[]
        for i in base:
            basepow.append(list(map(int,(i.split('^')))))
        return basepow'''
        return mono

    def __str__(self) -> str:
        pass

a=generator_experssion('-E_2^4E_1^3+E_2^3E_1^4+E_2^2E_1^5-E_2E_1^6+E_1^7')
print(a.SimplifyToMonomial())