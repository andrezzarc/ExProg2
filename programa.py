from funcoes import*
cartela = {
    'regra_simples':  {
        1:-1,
        2:-1,
        3:-1,
        4:-1,
        5:-1,
        6:-1
    },
    'regra_avancada' : {
        'sem_combinacao':-1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}
imprime_cartela(cartela)
for i in range (12):
    rolados = rolar_dados(5)
    guardados = []
    j = 0
    print(f"Dados rolados: {rolados}")
    print(f"Dados guardados: {guardados}")
    print ("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
    while True:
        acao = input()
        if acao == "1":
            print ("Digite o índice do dado a ser guardado (0 a 4):")
            n = input()
            resultado = guardar_dado(rolados,guardados,int(n))
            rolados = resultado[0]
            guardados = resultado[1]
            print(f"Dados rolados: {rolados}")
            print(f"Dados guardados: {guardados}")
            print ("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        elif acao == "2":
            print ("Digite o índice do dado a ser removido (0 a 4):")
            n = input()
            resultado = remover_dado(rolados,guardados,int(n))
            rolados = resultado[0]
            guardados = resultado[1]
            print(f"Dados rolados: {rolados}")
            print(f"Dados guardados: {guardados}")
            print ("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        elif acao == "3":
            if j >= 2:
                print ("Você já usou todas as rerrolagens.")
                print(f"Dados rolados: {rolados}")
                print(f"Dados guardados: {guardados}")
                print ("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            else:
                rolados = rolar_dados(len(rolados))
                j += 1
                print(f"Dados rolados: {rolados}")
                print(f"Dados guardados: {guardados}")
                print ("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        elif acao == "4":
            imprime_cartela(cartela)
            print(f"Dados rolados: {rolados}")
            print(f"Dados guardados: {guardados}")
            print ("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        elif acao == "0":
            print ("Digite a combinação desejada:")
            while True:
                combinacao = input()
                if combinacao.isdigit():
                    combinacao = int(combinacao)
                s = cartela["regra_simples"]
                a = cartela["regra_avancada"]
                if combinacao not in s and combinacao not in a:
                    print("Combinação inválida. Tente novamente.")
                elif (combinacao in a and a[combinacao] != -1) or (combinacao in s and s[combinacao] != -1):
                    print ("Essa combinação já foi utilizada.")
                else:
                    cartela = faz_jogada(rolados + guardados,combinacao,cartela)
                    break
            break
        else:
            print("Opção inválida. Tente novamente.")


total = 0
pontos_simples = 0
for valor in cartela["regra_simples"].values():
    if valor != -1:
        total += valor
        pontos_simples += valor
for valor in cartela["regra_avancada"].values():
    if valor != -1:
        total += valor

if pontos_simples >= 63:
    total += 35

imprime_cartela(cartela)
print (f"Pontuação total: {total}")





    
    

