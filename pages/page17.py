# função ObterFlorestaGeradora(G: Grafo): Grafo
  # var T: Grafo
  # V(T), E(T) ← V(G), ∅
  # BuscaCompleta(G)
  # para uv ∈ E(G) faça
    # se Descoberta[uv] então
    #   E(T) ← E(T) ∪ { uv }
  # retornar T
from importer import *

def ObterFlorestaGeradora(g: Graph) -> Graph:
  t = Graph(g.listVertices())
  info = BuscaCompleta(g)
  for e,v in info.descobertos.items():
    if(v == True):
      edge = EFromKey(e)
      t.AddE(edge[0],edge[1])
  #ou
  # for u,v in g.listEdges():
  #   if info.descobertos[EKey(u,v)]:
  #     t.AddE(u,v)
  return t
