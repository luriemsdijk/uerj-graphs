from importer import *
def BuscaCore(g: Graph, r: str, info: GraphInfo):
  info.visitados[r] = True
  for v, w in g.listEdges():
    if info.visitados[v] and not info.explorados[EKey(v,w)]:
      info.explorados[EKey(v,w)] = True
      if not info.visitados[w]:
        info.visitados[w], info.descobertos[EKey(v,w)] = True, True
  return info
