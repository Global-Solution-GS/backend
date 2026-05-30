#0. Menu -> Teotonio (ok)
#1. Resumo sobre o Climex -> Teotonio (ok)
#2. Cadastrar a regiao monitorada, contendo nome da regiao, temp media, indice de umidade [ALTA, MEDIA, BAIXA] e indice de harborizacao [ALTA, MEDIA, BAIXA] -> Teotonio
#3. Analise de vulnerabilidade climatica com base nos parametros acima -> Teotonio
#4. Retorno de todo os cadastros -> Alisson
#5. Analise ambiental com o levantamento por estado/regiao e indice de vulnerabilidade climatica -> Alisson
#6. Sugestao climatica para os casos extremos -> Alisson

regioes = []

def menu():
    while True:
        try:
            resposta = int(input("""
[1] - Resumo sobre o Climex
[2] - Cadastro de região para monitoramento ambiental
[3] - Análise de Vulnerabilidade climática
[4] - Listagem de todos os cadastros
[5] - Análise ambiental/região
[6] - Sugestões climáticas
[0] - Sair
"""))

            match resposta:
                case 1:
                    print(resumo_climex())
                case 2:
                    cadastro_regiao_monitorada()
                case 3:
                    print("Em desenvolvimento")
                case 4:
                    print("Em desenvolvimento")
                case 5:
                    print("Em desenvolvimento")
                case 6:
                    print("Em desenvolvimento")
                case 0:
                    print("Muito obrigado pela atenção!")
                    break
                case _:
                    print("Valor inválido, favor selecionar uma das opções do menu!")
        except ValueError:
            print("Valor inválido, favor selecionar uma das opções do menu!")


#Opção 1 do menu
def resumo_climex():
    return """
O ClimaX é uma plataforma inteligente de monitoramento climático urbano que integra APIs meteorológicas, sensores IoT e análise de dados em Python para identificar regiões vulneráveis a ilhas de calor e baixa umidade na Região Metropolitana de São Paulo. O sistema processa indicadores ambientais em tempo real para gerar mapas interativos, classificação de risco automático e alertas estratégicos, auxiliando órgãos públicos e comunidades na tomada de decisões preventivas e no planejamento de ações urbanas sustentáveis."""

#Opção 2 do menu
def cadastro_regiao_monitorada():
    try:
        while True:
            opcoes_indices = [1,2,3]

            regiao = input("Qual região você deseja cadastrar:\n").title().strip()
            
            while True:
                try:
                    temperatura_media = float(input("Qual a temperatura média da região informada:\n"))

                    if temperatura_media < -20 or temperatura_media > 50:
                        print("Temperatura inválida, favor selecionar uma temperatura válida")
                    else:
                        break
                except ValueError:
                    print("Entrada inválida, favor selecionar uma temperatura válida")

            while True:
                try:
                    indice_umidade = int(input(f"Qual o indice de umidade do ar da região informada: \n[1] - Alta\n[2] - Média\n[3] - Baixa\n"))

                    if indice_umidade in opcoes_indices:
                        break
                    print("Entrada inválida, favor selecionar uma opção entre 1 e 3")
                except ValueError:
                    print("Entrada inválida, favor selecionar um índice válido")


            while True:
                try:
                    indice_arborizacao = int(input(f"Qual o indice de arborização da região informada: \n[1] - Alto\n[2] - Médio\n[3] - Baixo\n"))

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

            print(f"Região cadastrada: {dict_regiao}")
            break

    except ValueError:
        print("Valor inválido, favor selecionar valores condizentes com o menu!")


menu()