# função TemCiclo(G: Grafo): Lógico
# BuscaCompleta(G)
# para uv ∈ E(G) faça
# se não Descoberta[uv] então
# retornar V
# retornar F

from importer import *

def TemCiclo(g: Graph):
  info = BuscaCompleta(g)
  for v,w in g.listEdges():
    if not info.descobertos[EKey(v,w)]:
      return True
  return False

# g =  readGraph()
# print("temCiclos", TemCiclo(g))
