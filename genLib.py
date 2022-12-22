class genClass:
    @staticmethod
    def minimal(str):
        temp=str
        '''i=0
        while i<len(temp)-1:
            if temp[i]=='f' and temp[i+1]=='E':
                temp=temp[:i]+'Ef'+temp[i+2:]
                if i>0:
                    i-=1
                else:
                    i=1
            elif temp[i]=='F' and temp[i+1]=='e':
                temp=temp[:i-1]+'eF'+temp[i+2:]
                if i>0:
                    i-=1
                else:
                    i=1
            else:
                i+=1'''
        return temp

    def __init__(self, str):
        self.str=genClass.minimal(str)

    def __str__(self) -> str:
        return self.str

    def __eq__(self, other):
        return self.str==other.str

    def __mul__(self, other):
        return genClass(self.str+other.str)
    #def simplify(self):
        