import random
def rolar_dados (n):
    lista= []
    for i in range(n):
        lista.append(random.randint(1,6))
    return (lista)

def guardar_dado (rolados,guardados,n):
    for i in range(len(rolados)):
        if n == i:
            guardados.append(rolados[i])
    res = [rolados, guarados]
    return res

    