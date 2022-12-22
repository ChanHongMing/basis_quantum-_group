def T1(array):
    for i in range(len(array)):
        coemono=array[i][0]
        powq=array[i][1]
        temp=array[i][2:]
        resultmono=[coemono,powq]
        for j in range(len(temp)):
            if temp[j]==1:
                resultmono[0]*=-1
                resultmono.append(3)
                resultmono.append(5)
            if temp[j]==2:
                coemono*=-1
                resultmono.append(3)
                resultmono.append(5)
