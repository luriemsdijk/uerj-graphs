# # função EhConexo(G: Grafo): Lógico
# #   Busca(G)
# #   para v ∈ V(G) faça
# #     se não Visitado[v] então
# #       retornar F
# #   retornar V

# from file import *
from importer import *

def EhConexo(g: Graph) -> bool:
  info = Busca(g)
  for v in g.listVertices():
    if not info.visitados[v]:
      return False
  return True
