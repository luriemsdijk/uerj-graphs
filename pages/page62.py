# procedimento DeterminarDistancias(G: Grafo, v: Inteiro):
#   var F: Fila
#   rotular (V(G), Dist: Inteiro)
#   Visitado[v], Dist[V(G)] ← V, ∞
#   enfileira(F, (v, 1))
#   enquanto tamanho(P) > 0 faça
#     (v, niv) ← desenfileira(F)
#     para w ∈ N(v) faça
#       se Visitado[w] então
#         se não Explorada[vw] então
#           Explorada[vw] ← V
#     senão
#       Explorada[vw], Descoberta[vw] ← V, V
#       Visitado[w], Dist[w] ← V, niv
#       enfileira(F, (w, niv+1))

from importer import *

def DeterminarDistancias(g: Graph, initial: str):
  F = Queue()
  info = GraphInfo(g.listVertices(),g.listEdges())
  info.visitados[initial] = True
  F.insert((initial,1))
  while (F.size() > 0):
    v, niv = F.pop()
    for w in g.getNeighborhood(v):
      if(info.visitados[w]):
        if(not info.explorados[EKey(v,w)]):
          info.explorados[EKey(v,w)] = True
      else:
        info.explorados[EKey(v,w)], info.descobertos[EKey(v,w)] = True, True
        info.visitados[w] = True
        if(info.distancias[w] is 0 and w is not initial): info.distancias[w] = niv # previne sobreescrever de distância
        F.insert((w, niv+1))
  return info
