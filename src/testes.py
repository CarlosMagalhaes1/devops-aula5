importação jogovelha
importação sys

erroInicializar = Falso
jogovelha  . inicializar()

se len(jogo) != 3:
        erroInicializar = True
outra coisa:
        para linha no jogo:
                se len(linha) != 3:
                        erroInicializar = True
                outra coisa:
                        para elemento em linha:
                                se elemento != '.':
                                        erroInicializar = True
se erroInicializar:
        sys. saída(1)
outra coisa:
        sys. saída(0)
