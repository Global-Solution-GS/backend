#Opçao 4
def todas_regioes():
    print("=" * 25)
    print("REGIÕES MONITORADAS")
    print("=" * 25)
    
    if not regioes:
        print("Nenhuma região cadastrada.")
        return 
    
    for indice, regiao in enumerate(regioes):
        print(f"{indice + 1})")
        print(f"Nome: {regiao["nome"]}")
        print(f"Temperatura: {regiao["temperatura"]}")
        print(f"Umidade: {regiao["umidade"]}")
        print(f"Arborização: {regiao["arborizacao"]}")
        print(f"Risco: {regiao["risco"]}")
    



        