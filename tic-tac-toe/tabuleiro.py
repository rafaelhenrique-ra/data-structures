# -*- coding: utf-8 -*-

class Tabuleiro:
    DESCONHECIDO = 0
    JOGADOR_0 = 1    # 'O' - soma alvo: 3 (1+1+1)
    JOGADOR_X = 4     # 'X' - soma alvo: 12 (4+4+4)
    
    def __init__(self):
        self.matriz = [[self.DESCONHECIDO, self.DESCONHECIDO, self.DESCONHECIDO],
                       [self.DESCONHECIDO, self.DESCONHECIDO, self.DESCONHECIDO],
                       [self.DESCONHECIDO, self.DESCONHECIDO, self.DESCONHECIDO]]
    
    def tem_campeao(self):
        # Verifica linhas
        for linha in self.matriz:
            soma = sum(linha)
            if soma == 3:
                return self.JOGADOR_0
            if soma == 12:
                return self.JOGADOR_X
        
        # Verifica colunas
        for coluna in range(3):
            soma = self.matriz[0][coluna] + self.matriz[1][coluna] + self.matriz[2][coluna]
            if soma == 3:
                return self.JOGADOR_0
            if soma == 12:
                return self.JOGADOR_X
        
        # Verifica diagonal principal
        soma = self.matriz[0][0] + self.matriz[1][1] + self.matriz[2][2]
        if soma == 3:
            return self.JOGADOR_0
        if soma == 12:
            return self.JOGADOR_X
        
        # Verifica diagonal secundária
        soma = self.matriz[0][2] + self.matriz[1][1] + self.matriz[2][0]
        if soma == 3:
            return self.JOGADOR_0
        if soma == 12:
            return self.JOGADOR_X
        
        # Verifica empate (velha)
        if all(celula != self.DESCONHECIDO for linha in self.matriz for celula in linha):
            return 0  # Código para empate
        
        return self.DESCONHECIDO  # Jogo ainda não terminou