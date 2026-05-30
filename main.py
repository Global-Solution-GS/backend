#0. Menu -> Teotonio
#1. Resumo sobre o Climex -> Teotonio
#2. Cadastrar a regiao monitorada, contendo nome da regiao, temp media, indice de umidade [ALTA, MEDIA, BAIXA] e indice de harborizacao [ALTA, MEDIA, BAIXA] -> Teotonio
#3. Analise de vulnerabilidade climatica com base nos parametros acima -> Teotonio
#4. Retorno de todo os cadastros -> Alisson
#5. Analise ambiental com o levantamento por estado/regiao e indice de vulnerabilidade climatica -> Alisson
#6. Sugestao climatica para os casos extremos -> Alisson

print("executando")

def menu():
    while True:
        try:
            resposta = int(input("""
[1] - Resumo sobre o Climex
[2] - Cadastro da região monitorada
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
                    print("Em desenvolvimento")
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



def resumo_climex():
    return """
O ClimaX é uma plataforma inteligente de monitoramento climático urbano que integra APIs meteorológicas, sensores IoT e análise de dados em Python para identificar regiões vulneráveis a ilhas de calor e baixa umidade na Região Metropolitana de São Paulo. O sistema processa indicadores ambientais em tempo real para gerar mapas interativos, classificação de risco automático e alertas estratégicos, auxiliando órgãos públicos e comunidades na tomada de decisões preventivas e no planejamento de ações urbanas sustentáveis."""

menu()