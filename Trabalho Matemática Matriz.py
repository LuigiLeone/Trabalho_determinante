matriz =  [[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 1]]

def leib(matriz):
    n = len(matriz)
    if n == 1:
        return matriz[0][0]
    else:
        soma = 0
        for j in range(n):
            nova_matriz = []
            for i in range(1, n):
                linha = []
                for k in range(n):
                    if k != j:
                        linha.append(matriz[i][k])
                nova_matriz.append(linha)
            sinal = (-1) ** j
            soma += matriz[0][j] * sinal * leib(nova_matriz)
        return soma

det = leib(matriz)

print("O determinante da matriz :", det)
