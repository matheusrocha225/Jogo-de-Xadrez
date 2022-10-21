def vaiCavalo( origemX, origemY, destinoX, destinoY ):
    # criamos uma matriz 8x8 preenchida com False
    # para anotar as casas ja testadas
    casasTestadas = [[False]*8 for i in range(8)]

    # todos os movimentos possiveis do cavalo
    movimentos = [[-1,-2],[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2]]

    # o primeiro passo e a origem do cavalo
    # X, Y e caminho percorrido ate entao (vazio no comeco)
    passos = [[origemX, origemY,[]]]

    while True:
        proximosPassos = []
        for passo in passos:
            print("Cavalo atualmente em [", passo[0], ",", passo[1], "], vindo de", passo[2])

            # vamos testar todos os movimentos possiveis a partir deste passo
            for movimento in movimentos:
                x = passo[0]+movimento[0]
                y = passo[1]+movimento[1]

                # armazenamos o caminho feito ate chegar aqui
                caminho = list(passo[2])
                caminho.append([passo[0],passo[1]])

                # o cavalo chegou ao destino, retornamos o caminho completo
                if x == destinoX and y == destinoY:
                    print("  PRONTO! Chegamos em [", x, y, "]")
                    caminho.append([x,y])
                    return caminho

                # senao, armazenamos a posicao para a proxima rodada
                elif 0 <= x < 8 and 0 <= y < 8 and not casasTestadas[x][y]:
                    print("  Destino nao encontrado em [", x, y, "], coordenadas na pilha")
                    proximosPassos.append([x,y,caminho])

                    # vamos descartar novas tentativas partindo daqui
                    casasTestadas[x][y] = True

        # todos os passos realizados, vamos para os seguintes
        passos = proximosPassos

print("\nCaminho feito:", vaiCavalo(3, 2, 3, 3))
