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

