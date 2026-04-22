import random
def rolar_dados (n):
    lista= []
    for i in range(n):
        lista.append(random.randint(1,6))
    return (lista)

def guardar_dado (rolados,guardados,n):

    resp = []
    for i in range(len(rolados)):
        if i != n:
            resp.append(rolados[i])
        elif n == i:
            guardados.append(rolados[i])
    ok = [resp, guardados]

    return ok

def remover_dado (rolados, guardados,n):
    rolados.append (guardados[n])
    guardados2= []
    for i in range (len (guardados)):
        if i != n:
            guardados2.append(guardados[i])
    final= [rolados, guardados2]
    return (final)

def calcula_pontos_regra_simples (faces):
    pontos = {}
    for i in range (1,7):
        pontos[i] = 0
    for i in faces:
        pontos[i] += i
    return pontos

def calcula_pontos_soma (lista):
    soma =0

    verificador=0
    for i in range (1,len(lista)):
        if lista[i]== lista[i-1]+1:
            verificador += 1
    if verificador == (len (lista)-1):
        if len (lista)==4:
            return (15)
        if len(lista)==5:
            return (15)
    
    valor=0 
    for i in range (len(lista)-5):
        if lista[i]==lista[i+1] and lista[i]==lista[i+2] and lista[i]==lista[i+3] and lista[i]==lista[i+4]:
            return (50)
    for i in range (len(lista)):
        soma += lista[i]
    return (soma)

def calcula_pontos_sequencia_baixa (l):
    for i in range (len(l)):
        numero= l[i]
        contador=0 
        a=0
        while a<len(l):
            if l[a] == numero +1:
                contador +=1
                numero += 1
                a=0
            else:
                a +=1
        if contador >= 3:
            return (15) 
    return (0)

def calcula_pontos_sequencia_alta (l):
    for i in range (len(l)):
        numero= l[i]
        contador=0 
        a=0
        while a<len(l):
            if l[a] == numero +1:
                contador +=1
                numero += 1
                a=0
            else:
                a +=1
        if contador >= 4:
            return (30) 
    return (0)

def calcula_pontos_full_house (l):
    soma2=0
    soma3=0
    for i in range (len(l)):
        soma= l[i]
        contador= 0
        a=0
        while a<len(l):
            if l[a]==l[i] and a != i:
                contador += 1
                soma += l[i]
            a += 1
        if contador == 1:
            soma2= soma
        elif contador == 2:
            soma3= soma
    if soma2 !=0 and soma3 != 0:
        return (soma2+soma3)
    else:
        return (0)

def calcula_pontos_quadra (l):
    soma=0
    resposta= ""
    for i in range (len(l)):
        contador= 0
        soma += l[i]
        for a in range (len(l)):
            if l[i]== l[a]:
                contador += 1
        if contador>=4:
            resposta= True
    if resposta == True:
        return (soma)
    return (0)


def calcula_pontos_quina (l):
    for i in range (len(l)):
        contador= 0
        for a in range (len(l)):
            if l[i]== l[a]:
                contador += 1
        if contador>=5:
            return (50)
    return (0)