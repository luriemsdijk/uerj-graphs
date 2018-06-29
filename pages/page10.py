# função TemCiclo(G: Grafo): Lógico
# BuscaCompleta(G)
# para uv ∈ E(G) faça
# se não Descoberta[uv] então
# retornar V
# retornar F

from importer import *
from page6 import BuscaCompleta
print("AINDA NÃO FUNCIONANDO")
def TemCiclo(g: Graph):
  info = BuscaCompleta(g)
  for v,w in g.listEdges():
    if not info.descobertos[makeE(v,w)]:
      return True
  return False

g =  readGraph()

print("temCiclos", TemCiclo(g))
