# Conta os algoritmos implementados com Matriz

from importer import *
from adjMatrix import *
from copy import copy
import time

g = readGraph()

#print(g)
inicio5=0.0
inicio6=0.0
inicio9=0.0
inicio10=0.0
inicio11=0.0
inicio12=0.0
inicio13=0.0
inicio17=0.0
inicio27=0.0
inicio57=0.0
inicio62 = 0.0
fim5=0.0
fim6=0.0
fim9=0.0
fim10=0.0
fim11=0.0
fim12=0.0
fim13=0.0
fim17=0.0
fim27=0.0
fim57=0.0
fim62 = 0.0


for i in range  (0,200):
    
    inicio5 += time.time()  
    Busca(g)
    fim5 += time.time()


    
    inicio6 += time.time()
    BuscaCompleta(g)
    fim6 += time.time()


    inicio9 += time.time()
    EhConexo(g)
    fim9 += time.time()

   
    inicio10 += time.time()
    TemCiclo(g)
    fim10 += time.time()

    
    inicio11 += time.time()
    EhFloresta(g)
    fim11 += time.time()

   
    inicio12 += time.time()
    EhArvore(g)
    fim12 += time.time()

    
    inicio13 += time.time()
    EhArvore2(g)
    fim13 += time.time()

   
    inicio17 += time.time()
    ObterFlorestaGeradora(g)
    fim17 += time.time()

    # Quebrado
    #inicio26 = time.time()
    #BuscaProfundidadeI(g, '1')
    #fim26 = time.time()

  
    inicio27 += time.time()
    BuscaProfundidadeR(g, '1')
    fim27 += time.time()

    
    inicio57 += time.time()
    BuscaLargura(g, '1')
    fim57 += time.time()

    
    inicio62 += time.time()
    DeterminarDistancias(g,'1')
    fim62 += time.time()



#print()
#print("Page5: Busca")
#print(busca)
#print()
#print("Page6: BuscaCompleta")
#print(buscacompleta)
#print()
#print("Page9: é Conexo")
#print(EhConexo)
#print()
#print("Page10: Tem ciclo")
#print(TemCiclo)
#print()
#print("Page11: É Floresta")
#print(EhFloresta)
#print()
#print("Page12: É Arvore")
#print(EhArvore)
#print()
#print("Page13: É Arvore usando ciclo e conexo")
#print(EhArvore2)
#print()
#print("Page17: Obter floresta geradora")
#print(ObterFlorestaGeradora)
#print()
#print("Page27: Busca por profundidade Recursivo")
#print(BuscaProfundidadeR)
#print()
#print("Page57: Busca por largura")
#print(BuscaLargura)
#print()
#print("Page62: Determinar distância")
#print(DeterminarDistancias)
#print()

print("Time Page5:",(fim5 - inicio5)/200)
print("Time Page6:",(fim6 - inicio6)/200)
print("Time Page9:",(fim9 - inicio9)/200)
print("Time Page10:",(fim10 - inicio10)/200)
print("Time Page11:",(fim11 - inicio11)/200)
print("Time Page12:",(fim12 - inicio12)/200)
print("Time Page13:",(fim13 - inicio13)/200)
print("Time Page17:",(fim17 - inicio17)/200)
#print("Time Page26:",(fim26 - inicio26)/200)
print("Time Page27:",(fim27 - inicio27)/200)
print("Time Page57:",(fim57 - inicio57)/200)
print("Time Page62:",(fim62 - inicio62)/200)
