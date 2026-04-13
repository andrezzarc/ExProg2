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
