# testa os algoritmos implementados

from importer import *
from adjList import *
from copy import copy

g = readGraph()

print(g)

print()
print("Page5: Busca")
print(Busca(g))

print()
print("Page6: BuscaCompleta")
print(BuscaCompleta(g))

print()
print("Page9: é Conexo")
print(EhConexo(g))

print()
print("Page10: Tem ciclo")
print(TemCiclo(g))

print()
print("Page11: É Floresta")
print(EhFloresta(g))

print()
print("Page12: É Arvore")
print(EhArvore(g))

print()
print("Page13: É Arvore usando ciclo e conexo")
print(EhArvore2(g))

print()
print("Page17: Obter floresta geradora")
print(ObterFlorestaGeradora(g))

# Quebrado
# print()
# print("Page26: Busca por profundidade Iterativo")
# print(BuscaProfundidadeI(g, '1'))

print()
print("Page27: Busca por profundidade Recursivo")
print(BuscaProfundidadeR(g, '1'))

print()
print("Page57: Busca por largura")
print(BuscaLargura(g, '1'))

print()
print("Page62: Determinar distância")
print(DeterminarDistancias(g,'1'))

