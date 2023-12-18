'''
guanya={'r':'s','s':'p','p':'r'}

while True: 
    TiradaJugA=input('r/p/s: ')
    TiradaJugB=input('r/p/s: ')
    if TiradaJugA==TiradaJugB:
        print ('empat!')
    elif guanya[TiradaJugA]==TiradaJugB:
        print('guanya A!')
    else:
        print('guanya B!') 

dcomarca={}
dcomarca['vic']='osona'
dcomarca['bcn']='barcelonès'
dcomarca['salt']='gironès'
dcomarca['girona']='gironès'
dcomarca['manlleu']='osona'

dcom_inv={}
for poble,comarca in dcomarca.items():
    if comarca in dcom_inv:
        dcom_inv[comarca].append(poble)
    else:
        dcom_inv[comarca]=[poble]

lpobles=dcom_inv['gironès']
print(lpobles)
'''
'''
for poble,comarca in dcomarca.items():
    if comarca=='osona':
        print(poble)
'''    
'''
def Xifrar(frase,dicc):
    frase_xifrada=''
    for lletra in frase:
        frase_xifrada+=dicc[lletra]
    return frase_xifrada

def InvertirDicc(d1):
    d2={}
    for k,v in d1.items():
        d2[v]=k
    return d2

dicc_xifrat={'a':'w', 'b':'o', 'c':'j', 'd':'x', 'e':'p', 'f':'l', 'g':' ', 'h':'g', 'i':'z', 'j':'b', 'k':'a', 'l':'m', 'm':'t', 'n':'v', 'o':'h', 'p':'f', 'q':'r', 'r':'y', 's':'e', 't':'u', 'u':'q', 'v':'c', 'w':'k', 'x':'s', 'y':'i', 'z':'n', ' ':'d'}
dicc_invertit=InvertirDicc(dicc_xifrat)

frase_original="aquest es el missatge"
frase_xifrada=Xifrar(frase_original,dicc_xifrat)
frase_desxifrada=Xifrar(frase_xifrada,dicc_invertit)

print (frase_xifrada)
print(frase_desxifrada)



frase_original="aquest es el missatge"
frase_xifrada=''
for lletra in frase_original:
    frase_xifrada+=dicc_xifrat[lletra]
print(frase_original)
print(frase_xifrada)

d={'a':10,'b':20,'c':30}
di={}
for k,v in d.items():
    di[v]=k


frase="hola gent com aneu esteu tots be?"
d={} #diccionari buit
for c in frase:
    if c not in d:
        d[c]=1
    else:
        d[c]+=1
lk=list(d.keys())
lk.sort() #ordena 
print(lk)
for k in lk:
    print (k,d[k])
'''