class laurent_polynomial:
    def __init__(self,coe,power,base='x'):
        self.coe = coe
        self.power = power
        self.rank = max(power)
        self.base = base

    def __add__(self,other):
        if self.rank >= other.rank:
            coe = self.coe
            power = self.power
            for i in range(len(other.coe)):
                if other.power[i] in power:
                    coe[power.index(other.power[i])] += other.coe[i]
                else:
                    coe.append(other.coe[i])
                    power.append(other.power[i])
        else:
            coe = other.coe
            power = other.power
            for i in range(len(self.coe)):
                if self.power[i] in power:
                    coe[power.index(self.power[i])] += self.coe[i]
                else:
                    coe.append(self.coe[i])
                    power.append(self.power[i])
        return laurent_polynomial(coe,power,self.base)

    def __sub__(self,other):
        if self.rank >= other.rank:
            coe = self.coe
            power = self.power
            for i in range(len(other.coe)):
                if other.power[i] in power:
                    coe[power.index(other.power[i])] -= other.coe[i]
                else:
                    coe.append(-other.coe[i])
                    power.append(other.power[i])
        else:
            coe = [-i for i in other.coe]
            power = other.power
            for i in range(len(self.coe)):
                if self.power[i] in power:
                    coe[power.index(self.power[i])] += self.coe[i]
                else:
                    coe.append(self.coe[i])
                    power.append(self.power[i])
        return laurent_polynomial(coe,power,self.base)

    def __mul__(self,other):
        coe = []
        power = []
        for i in range(len(self.coe)):
            for j in range(len(other.coe)):
                if self.power[i] + other.power[j] in power:
                    coe[power.index(self.power[i] + other.power[j])] += self.coe[i] * other.coe[j]
                else:
                    coe.append(self.coe[i] * other.coe[j])
                    power.append(self.power[i] + other.power[j])
        return laurent_polynomial(coe,power,self.base)

    def evaluate(self,input):
        eva=0
        for i in range(len(self.coe)):
            eva+=self.coe[i]*(input**self.power[i])
        return eva

    def add_inverse(self):
        coe = [-i for i in self.coe]
        power = self.power
        return laurent_polynomial(coe,power,self.base)

    def __eq__(self,other):
        
        
    
k=laurent_polynomial([1,2.5,3.92],[0,-1,2.5])
q=laurent_polynomial([-1,7.3,8],[0,1,2])
print((k+q).coe)
print((k+q).power)
        