#0. Menu -> Teotonio (ok)
#1. Resumo sobre o Climex -> Teotonio (ok)
#2. Cadastrar a regiao monitorada, contendo nome da regiao, temp media, indice de umidade [ALTA, MEDIA, BAIXA] e indice de harborizacao [ALTA, MEDIA, BAIXA] -> Teotonio
#3. Analise de vulnerabilidade climatica com base nos parametros acima -> Teotonio
#4. Retorno de todo os cadastros -> Alisson
#5. Analise ambiental com o levantamento por estado/regiao e indice de vulnerabilidade climatica -> Alisson
#6. Sugestao climatica para os casos extremos -> Alisson

regioes = []
regioes_criticas = []

def menu():
    while True:
        try:
            resposta = int(input(f"""\n[1] - Resumo sobre o Climex
[2] - Cadastro de região para monitoramento ambiental
[3] - Análise de Vulnerabilidade climática
[4] - Listagem de todos os cadastros
[5] - Análise ambiental/região
[6] - Sugestões climáticas
[0] - Sair
"""))

            match resposta:
                case 1:
                    mensagem_retorno = resumo_climex()
                    print(f"\n{mensagem_retorno}")
                case 2:
                    opcoes_indices = [1,2,3]
                    dict_cadastrado = cadastro_regiao_monitorada(opcoes_indices)
                    print(f"\nRegião cadastrada: {dict_cadastrado}")
                case 3:
                    mensagem_retorno = analisa_vulnerabilidade_climatica()
                    print(f"\n{mensagem_retorno}")
                case 4:
                    listar_regioes()
                case 5:
                    gerar_relatorio()
                case 6:
                    gerar_recomendacao()
                case 0:
                    print("Muito obrigado pela atenção!")
                    break
                case _:
                    print("Valor inválido, favor selecionar uma das opções do menu!")
        except ValueError:
            print("Valor inválido, favor selecionar uma das opções do menu!")


#Opção 1 do menu
def resumo_climex():
    return """O ClimaX é uma plataforma inteligente de monitoramento climático urbano que integra APIs meteorológicas, sensores IoT e análise de dados em Python para identificar regiões vulneráveis a ilhas de calor e baixa umidade na Região Metropolitana de São Paulo. O sistema processa indicadores ambientais em tempo real para gerar mapas interativos, classificação de risco automático e alertas estratégicos, auxiliando órgãos públicos e comunidades na tomada de decisões preventivas e no planejamento de ações urbanas sustentáveis."""

#Opção 2 do menu
def cadastro_regiao_monitorada(opcoes_indices):
    try:
        regiao = input("\nQual região você deseja cadastrar:\n").title().strip()
        
        while True:
            try:
                temperatura_media = float(input("\nQual a temperatura média da região informada:\n"))

                if temperatura_media < -20 or temperatura_media > 50:
                    print("Temperatura inválida, favor selecionar uma temperatura válida")
                else:
                    break
            except ValueError:
                print("Entrada inválida, favor selecionar uma temperatura válida")

        while True:
            try:
                indice_umidade = int(input(f"\nQual o indice de umidade do ar da região informada: \n[1] - Alta\n[2] - Média\n[3] - Baixa\n"))

                if indice_umidade in opcoes_indices:
                    break
                print("Entrada inválida, favor selecionar uma opção entre 1 e 3")
            except ValueError:
                print("Entrada inválida, favor selecionar um índice válido")


        while True:
            try:
                indice_arborizacao = int(input(f"\nQual o indice de arborização da região informada: \n[1] - Alto\n[2] - Médio\n[3] - Baixo\n"))

                if indice_arborizacao in opcoes_indices:
                    break
                print("Entrada inválida, favor selecionar uma opção entre 1 e 3")
            except ValueError:
                print("Entrada inválida, favor selecionar um índice válido")

        risco = "Não Analisado"

        dict_regiao = {
            "nome": regiao, 
            "temperatura": temperatura_media,
            "umidade": indice_umidade,
            "arborizacao": indice_arborizacao,
            "risco": risco
        }
        regioes.append(dict_regiao)

        return dict_regiao
    except ValueError:
        print("Valor inválido, favor selecionar valores condizentes com o menu!")

#Opção 3 do menu
def analisa_vulnerabilidade_climatica():
    if not regioes:
        return "Nenhuma região cadastrada para análise."

    for obj in regioes:
        umidade = obj["umidade"]
        arborizacao = obj["arborizacao"]
        temperatura = obj["temperatura"]  

        if (umidade == 3 and arborizacao == 3) or (umidade == 3 and arborizacao == 2) or (umidade == 2 and arborizacao == 3):
            obj["risco"] = "Crítico"

        elif (umidade == 1 and arborizacao == 1) or (umidade == 1 and arborizacao == 2) or (umidade == 2 and arborizacao == 1):
            obj["risco"] = "Baixo"

        else:
            obj["risco"] = "Moderado"

        if temperatura >= 30.0:
            if obj["risco"] == "Moderado":
                obj["risco"] = "Crítico"
            elif obj["risco"] == "Baixo":
                obj["risco"] = "Moderado"

        elif temperatura <= 18.0:
            if obj["risco"] == "Crítico":
                obj["risco"] = "Moderado"
            elif obj["risco"] == "Moderado":
                obj["risco"] = "Baixo"

        if(obj["risco"] == "Crítico"):
            regioes_criticas.append(obj["nome"])                

    return "Análise de vulnerabilidade climática atualizada para todas as regiões!"

#Opçao 4 do menu
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
        print(f"Umidade: {valida_indice(regiao["umidade"], "Umidade")}")
        print(f"Arborização: {valida_indice(regiao["arborizacao"], "Arborização")}")
        print(f"Risco: {regiao["risco"]}")

#Opção 5 do menu
def gerar_relatorio():
    if not regioes:
        print("Nenhuma região cadastrada.")
        return 
    
    print("=" * 25)
    print("RELATÓRIO AMBIENTAL")
    print("=" * 25)
    
    print(f"Total de regiões: {len(regioes)}")
    
    alto = 0
    medio = 0
    baixo = 0
    nao_definido = 0
    temperatura_soma = 0

    for regiao in regioes:
        if regiao["risco"] == "Baixo": baixo += 1
        elif regiao["risco"] == "Moderado": medio += 1
        elif regiao["risco"] == "Crítico": 
            alto += 1
        else: nao_definido +=1
        temperatura_soma += regiao["temperatura"]
        
    print(f"Risco Baixo: {baixo}")
    print(f"Risco Moderado: {medio}")
    print(f"Risco Crítico: {alto}")
    print(f"Risco Não Definido: {nao_definido}")
    
    print(f"Temperatura Média: {temperatura_soma / len(regioes):.1f}°C")
    
    print("Regiões mais vulneráveis: ")
    if not regioes_criticas:
        print("Não existe nenhuma região vulnerável cadastrada hoje.")
    else:
        for indice, i in enumerate(regioes_criticas, start= 1):
            print(f"{indice}) {i}")

#Opção 6 do menu
def gerar_recomendacao():
    print("=" * 25)
    print("RECOMENDAÇÕES SUSTENTÁVEIS")
    print("=" * 25)
    
    print("Regiões: ")
    
    if not regioes_criticas:
        print("Não existe nenhuma região vulnerável cadastrada!")
    else:
        for indice, i in enumerate(regioes_criticas, start= 1):
            print(f"{indice}) {i}")
        print("Nível de risco: CRÍTICO")
        print("Ações sugeridas: ")
        print("Aumentar arborização urbana\nCriar áreas verdes\nImplantar hortas comunitárias\nIntensificar monitoramento climático\nInstalar sensores ambientais")

def valida_indice(valor, tipo):
    if(valor == 1 and tipo == "Umidade"):
        return "Alta"
    elif(valor == 2 and tipo == "Umidade"):
        return "Média"
    elif(valor == 3 and tipo == "Umidade"):
        return "Baixa"

    elif(valor == 1 and tipo == "Arborização"):
        return "Alto"
    elif(valor == 2 and tipo == "Arborização"):
        return "Médio"
    elif(valor == 3 and tipo == "Arborização"):
        return "Baixo"


menu()