'''
Created on 11/08/2012

@author: giulliano
'''

from random import uniform
import random
from collections import deque

class GeradorJogo(object):

    def __init__(self):
        pass

    def randomico(self):
        jogo = deque()
        while len(jogo) != 5: 
            bola = int(uniform(1,15))
            if bola not in jogo:
                jogo.append(bola)
        while len(jogo) != 10: 
            bola = int(uniform(10,20))
            if bola not in jogo:
                jogo.append(bola)
        while len(jogo) != 15: 
            bola = int(uniform(15,25))
            if bola not in jogo:
                jogo.append(bola)        
        return sorted(list(jogo));

    def completar_jogo(self, jogo):
        if len(jogo) == 15:
            return jogo

        if len(jogo) > 15:
            novo_jogo = deque()
            for j in range(15):
                novo_jogo.append(jogo[j])
            return novo_jogo

        while len(jogo) < 15:
            bola = int(uniform(1,25))
            if bola not in jogo:
                jogo.append(bola)

        return jogo;

    def randomico_com_melhores_repeticoes(self, pergunta, repeticoes=7):
        jogo = deque()
        mes = random.randint(1, 12)
        ano = random.randint(2003, 2014)
        bolas = pergunta.repeticao_numeros(repeticoes, mes, ano);
        for melhores in bolas:
            jogo.append(melhores)
        return jogo;

    def randomico_com_melhores_colunas(self, pergunta, coluna=2):
        jogo = deque()
        bolas = pergunta.repeticao_numeros_coluna(coluna);
        for melhores in bolas:
            jogo.append(melhores)
        return jogo;

    def jogo_com_percentual_de(self, analisador, pergunta, percentual):
        p = 0
        while (p < percentual):
            jogo = deque()
            x = int(uniform(1,5))
            ca = int(uniform(1,5))
            jogo1 = self.randomico_com_melhores_repeticoes(pergunta, x)
            jogo2 = self.randomico_com_melhores_colunas(pergunta, ca)

            aux = [j for j in jogo1]
            aux += [j for j in jogo2]

            for j in aux:
                if j not in jogo:
                    jogo.append(j)

            jogo = self.completar_jogo(jogo);
            sorted(jogo)
            p = analisador.analisar_probabilidade_jogo(jogo)
        return jogo;
