# procedimento Busca(G: Grafo):
#   rotular (V(G), Visitado: Lógico)
#   rotular (E(G), Explorada: Lógico)
#   rotular (E(G), Descoberta: Lógico)
#   Visitado[V(G)] ← F; Explorada[E(G)] ← F; Descoberta[E(G)] ← F
#   r ← 1 // raiz pode ser qualquer vértice
#   Busca(G, r)

# procedimento Busca(G: Grafo, r: Inteiro):
#   Visitado[r] ← V
#   para vw ∈ E(G) tal que Visitado[v] e não Explorada[vw] faça
#     Explorada[vw] ← V
#       se não Visitado[w] então
#         Visitado[w], Descoberta[vw] ← V, V

from importer import *
# from buscaCore import BuscaCore

def Busca(g: Graph) -> GraphInfo:
  info = GraphInfo(g.listVertices(),g.listEdges())
  r = g.listVertices()[0]
  return BuscaCore(g,r, info)
