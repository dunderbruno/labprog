# -*- coding: utf-8 -*-

u"""
Arquivos.

Quantidade mínima possível de pastas
de tamanho B para armazenar N arquivos

Aluno: Bruno Olimpio dos Santos.
e-mail: belbrunosantos@gmail.com
"""


N, B = input().split(' ')
N = int(N)
B = int(B)
arquivos = input().split(' ')
arquivos = [int(i) for i in arquivos]
arquivos.sort(reverse=True)
