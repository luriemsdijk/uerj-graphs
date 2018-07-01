# procedimento BuscaLargura(G: Grafo, v: Inteiro):
# var F: Fila
# Visitado[v] ← V
# enfileira(F, v)
# enquanto tamanho(F) > 0 faça
#   v ← desenfileira(F)
#   para w ∈ N(v) faça
#     se Visitado[w] então
#       se não Explorada[vw] então
#         Explorada[vw] ← V
#     senão
#       Explorada[vw], Descoberta[vw] ← V, V
#       Visitado[w] ← V
#       enfileira(F, w)

from importer import *

def BuscaLargura(g: Graph, v: str):
  F = Queue()
  info = GraphInfo(g.listVertices(),g.listEdges())
  info.visitados[v] = True
  F.insert(v)
  while (F.size() > 0):
    v = F.pop()
    for w in g.getNeighborhood(v):
      if(info.visitados[w]):
        if(not info.explorados[EKey(v,w)]):
          info.explorados[EKey(v,w)] = True
      else:
        info.explorados[EKey(v,w)], info.descobertos[EKey(v,w)] = True, True
        info.visitados[w] = True
        F.insert(w)
  return info
