#Opçao 4
def listar_regioes():
    print("\n")
    print("=" * 25)
    print("REGIÕES MONITORADAS")
    print("=" * 25)
    print("\n")
    
    if not regioes:
        print("Nenhuma região cadastrada.")
        return 
    
    for indice, regiao in enumerate(regioes, start=1):
        print(f"{indice})")
        print(f"Nome: {regiao["nome"]}")
        print(f"Temperatura: {regiao["temperatura"]}")
        print(f"Umidade: {regiao["umidade"]}")
        print(f"Arborização: {regiao["arborizacao"]}")
        print(f"Risco: {regiao["risco"]}")
    
#Opção 5 do menu
def gerar_relatorio():
    print("\n")
    if not regioes:
        print("Nenhuma região cadastrada.")
        return 
    
    print("=" * 25)
    print("RELATÓRIO AMBIENTAL")
    print("=" * 25)
    print("\n")
    
    print(f"Total de regiões: {len(regioes)}")
    
    alto = 0
    medio = 0
    baixo = 0
    temperatura_soma = 0
    regioes_criticas = []
    
    
    for regiao in regioes:
        if regiao["risco"] == "Baixo": baixo += 1
        elif regiao["risco"] == "Moderado": medio += 1
        elif regiao["risco"] == "Crítico": 
            alto += 1
            regioes_criticas.append(regiao["nome"])
        temperatura_soma += regiao["temperatura"]
        
    print(f"Risco Baixo: {baixo}")
    print(f"Risco Moderado: {medio}")
    print(f"Risco Crítico: {alto}")
    
    print(f"Temperatura Média: {temperatura_soma / len(regioes):.1f}°C")
    
    print("Regiões mais vulneráveis: ")
    if not regioes_criticas:
        print("Parabéns não existe nenhuma região vulnerável")
    else:
        for indice, i in enumerate(regioes_criticas, start= 1):
            print(f"{indice}) {i}")
        
#Opção 6 do menu
def recomendacao():
    print("=" * 25)
    print("RECOMENDAÇÕES SUSTENTÁVEIS")
    print("=" * 25)
    
    print("Regiões: ")
    
    if not regioes_criticas:
        print("Parabéns não existe nenhuma região vulnerável")
    else:
        for indice, i in enumerate(regioes_criticas, start= 1):
            print(f"{indice}) {i}")
        print("Nível de risco: CRÍTICO")
    
    
    print("Ações sugeridas: ")
    print("✓ Aumentar arborização urbana\n✓ Criar áreas verdes\n✓ Implantar hortas comunitárias\n✓ Intensificar monitoramento climático\n✓ Instalar sensores ambientais")
    