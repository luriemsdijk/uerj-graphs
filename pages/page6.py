
from importer import *

# procedimento BuscaCompleta(G: Grafo):
# rotular (V(G), Visitado: Lógico)
# rotular (E(G), Explorada: Lógico)
# rotular (E(G), Descoberta: Lógico)
# Visitado[V(G)] ← F; Explorada[E(G)] ← F; Descoberta[E(G)] ← F
# para r ← 1 até G.n faça
# se não Visitado[r] faça
# Busca(G, r)

from importer import *

def BuscaCompleta(g: Graph):
  info = GraphInfo()
  for v in g.listVertices():
    info.visitados[v] = False
  for v, w in g.listEdges():
    info.explorados[EKey(v,w)] = False
    info.descobertos[EKey(v,w)] = False
  for v in (v for v in g.listVertices() if not info.visitados[v]):
    BuscaCore(g,v, info)
  return info

