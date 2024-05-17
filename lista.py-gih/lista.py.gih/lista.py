# Criando um lita de nomes
nome = ["Alisson", "Bernardo", "Bianca", "Heloisa", "Bruno"]

# Exibindo a lista completa de nomes
print("Lista de nomes:", nome)

# Adicionando uma nova nome lista
nome.append("Giovanna")
print("depois de adicionar Giovanna:", nome)

# Removendo um nome da lista
nome.remove("Bruno")
print("Depois de remover Bruno:", nome)

# Acessando um nome específicao (primeiro nome)
primeiro_nome = nome[0]
print("A primeiro nome é:", nome)

# Percorrendo a lista de nome
print("Todas as frutas:")
for fruta in nome:
    print(nome)

# Verificando se um nome esta na lista     
    if "Giovanna" in nome: 
        print("Giovanna esta na lista de nome.")
    else:
        print("Giovanna não esta na lista de nome.")   

# Ordenando a lista de nome
nome.sort()
print("Lista de nome ordenada:", nome)

# Contando o número de nomes
numero_de_nome = len(nome)
print("Número de nome na lista:", numero_de_nome)