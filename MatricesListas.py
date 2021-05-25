

def llenarMatriz(t) :
    m=[]
    for i in range(0,t):
            a=[]
            for j in range(0,t) :
                if i==j :
                   a.append(1)
                else:
                   a.append(0)
            m.append(a)        
    return m

def llenarMatrizDS(t) :
    m=[]
    for i in range(0,t):
            a=[]
            for j in range(0,t) :
                if j==(t-2)-i:
                   a.append(1)
                else:
                   a.append(0)
            m.append(a)        
    return m
    

def mostrarMatriz(m):
    for i in range(0,len(m)):
        for j in range(0,len(m[i])) :
            print(m[i][j],end='')
        print ("")

'''
def llenarDP(m,t) :    
    for i in range(0,t):           
        for j in range(0,t) :                      
    '''
        



ma=llenarMatrizDS(20)
mostrarMatriz(ma,20) 



