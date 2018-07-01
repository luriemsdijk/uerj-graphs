# função EhArvore(G: Grafo): Lógico
  # Busca(G)
  # para v ∈ V(G) faça
    # se não Visitado[v] então
      # retornar F
  # para uv ∈ E(G) faça
  #   se não Descoberta[uv] então
        # retornar F
  # retornar V
from importer import *

def EhArvore(g: Graph) -> bool:
  info = Busca(g)
  for v in g.listVertices():
    if not info.visitados[v]:
      return False
  for u, v in g.listEdges():
    if not info.descobertos[EKey(u,v)]:
      return False

  return True

#
# print("EhArvore", EhArvore(g))
