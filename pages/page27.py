# procedimento BuscaProfundidade(G: Grafo, v: Inteiro):
#   Visitado[v] ← V
#   para w ∈ N(v) faça
#     se Visitado[w] então
#       se não Explorada[vw] então
#         Explorada[vw] ← V
#     senão
#       Explorada[vw], Descoberta[vw] ← V, V
#       BuscaProfundidade(G, w)

from importer import *

def BuscaProfundidadeR(g: Graph, v: str, info: GraphInfo = None):
  if(info == None): info = GraphInfo(g.listVertices(),g.listEdges())
  info.visitados[v] = True
  for w in g.getNeighborhood(v):
    if(info.visitados[w]):
      info.explorados[EKey(v,w)] = True
    else:
      info.explorados[EKey(v,w)], info.descobertos[EKey(v,w)] = True, True
      BuscaProfundidadeR(g,w,info)
  return info

#
# print(BuscaProfundidade(g,'1'))
