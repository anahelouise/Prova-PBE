lista = [1, 1, 2, 3, 4, 4, 5, 1]

comprimento_primeira_parte = int(input("Comprimento da primeira parte da lista: "))

primeira_parte = lista[:comprimento_primeira_parte]
segunda_parte = lista[comprimento_primeira_parte:]

print(f"Dividiu a referida lista em duas partes: ({primeira_parte}, {segunda_parte})")