# -*- coding: utf-8 -*-
from random import choice
from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro: Tabuleiro, tipo: int):
        super().__init__(tabuleiro, tipo)

    def getJogada(self) -> (int, int):
        # R1: Se voce ou o oponente tiver dois em sequência, complete a linha.
        jogada = self.verificar_dois_em_sequencia()
        if jogada:
            return jogada

        # R2: Se houver uma jogada que crie duas sequencias de duas marcacoes, use-a.
        jogada = self.verificar_duas_sequencias()
        if jogada:
            return jogada

        # R3: Se o quadrado central estiver livre, marque-o.
        if self.matriz[1][1] == Tabuleiro.DESCONHECIDO:
            return (1, 1)

        # R4: Se o oponente tiver marcado um canto, marque o canto oposto.
        jogada = self.verificar_canto_oposto()
        if jogada:
            return jogada

        # R5: Se houver um canto vazio, marque-o.
        jogada = self.verificar_canto_vazio()
        if jogada:
            return jogada

        # R6: Marque qualquer quadrado vazio.
        return self.escolher_quadrado_aleatorio()

    def verificar_dois_em_sequencia(self):
        for jogador in [self.tipo, self.tipo_oponente()]:
            for linha in range(3):
                valores = [self.matriz[linha][col] for col in range(3)]
                if valores.count(jogador) == 2 and Tabuleiro.DESCONHECIDO in valores:
                    coluna = valores.index(Tabuleiro.DESCONHECIDO)
                    return (linha, coluna)

            for coluna in range(3):
                valores = [self.matriz[lin][coluna] for lin in range(3)]
                if valores.count(jogador) == 2 and Tabuleiro.DESCONHECIDO in valores:
                    linha = valores.index(Tabuleiro.DESCONHECIDO)
                    return (linha, coluna)

            diagonal1 = [self.matriz[i][i] for i in range(3)]
            if diagonal1.count(jogador) == 2 and Tabuleiro.DESCONHECIDO in diagonal1:
                pos = diagonal1.index(Tabuleiro.DESCONHECIDO)
                return (pos, pos)

            diagonal2 = [self.matriz[i][2-i] for i in range(3)]
            if diagonal2.count(jogador) == 2 and Tabuleiro.DESCONHECIDO in diagonal2:
                pos = diagonal2.index(Tabuleiro.DESCONHECIDO)
                return (pos, 2-pos)

        return None

    def verificar_duas_sequencias(self):
        for linha in range(3):
            for coluna in range(3):
                if self.matriz[linha][coluna] == Tabuleiro.DESCONHECIDO:

                    self.matriz[linha][coluna] = self.tipo
                    contador = self.contar_sequencias_de_dois()

                    self.matriz[linha][coluna] = Tabuleiro.DESCONHECIDO
                    if contador >= 2:
                        return (linha, coluna)
        return None

    def contar_sequencias_de_dois(self):
        count = 0

        for linha in range(3):
            if self.matriz[linha].count(self.tipo) == 2 and Tabuleiro.DESCONHECIDO in self.matriz[linha]:
                count += 1


        for coluna in range(3):
            valores = [self.matriz[lin][coluna] for lin in range(3)]
            if valores.count(self.tipo) == 2 and Tabuleiro.DESCONHECIDO in valores:
                count += 1


        diagonal1 = [self.matriz[i][i] for i in range(3)]
        if diagonal1.count(self.tipo) == 2 and Tabuleiro.DESCONHECIDO in diagonal1:
            count += 1

        diagonal2 = [self.matriz[i][2-i] for i in range(3)]
        if diagonal2.count(self.tipo) == 2 and Tabuleiro.DESCONHECIDO in diagonal2:
            count += 1

        return count

    def verificar_canto_oposto(self):
        cantos = [(0, 0), (0, 2), (2, 0), (2, 2)]
        opostos = {(0, 0): (2, 2), (0, 2): (2, 0), (2, 0): (0, 2), (2, 2): (0, 0)}
        
        for canto in cantos:
            l, c = canto
            if self.matriz[l][c] == self.tipo_oponente():
                oposto = opostos[canto]
                if self.matriz[oposto[0]][oposto[1]] == Tabuleiro.DESCONHECIDO:
                    return oposto
        return None

    def verificar_canto_vazio(self):
        cantos = [(0, 0), (0, 2), (2, 0), (2, 2)]
        for canto in cantos:
            l, c = canto
            if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                return (l, c)
        return None

    def escolher_quadrado_aleatorio(self):
        vazios = []
        for l in range(3):
            for c in range(3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    vazios.append((l, c))
        return choice(vazios) if vazios else None

    def tipo_oponente(self):
        return Tabuleiro.JOGADOR_0 if self.tipo == Tabuleiro.JOGADOR_X else Tabuleiro.JOGADOR_X