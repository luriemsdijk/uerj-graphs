
from importer import *

# procedimento BuscaCompleta(G: Grafo):
# rotular (V(G), Visitado: Lógico)
# rotular (E(G), Explorada: Lógico)
# rotular (E(G), Descoberta: Lógico)
# Visitado[V(G)] ← F; Explorada[E(G)] ← F; Descoberta[E(G)] ← F
# para r ← 1 até G.n faça
# se não Visitado[r] faça
# Busca(G, r)


g = readGraph()

def BuscaCompleta(g: Graph):
  info = GraphInfo()
  for v in g.listVertices():
    info.visitados[v] = False
  for v, w in g.listEdges():
    info.explorados[makeE(v,w)] = False
    info.descobertos[makeE(v,w)] = False
  for v in (v for v in g.listVertices() if not info.visitados[v]):
    Busca2(g,v, info)
  return info

def Busca2(g: Graph, r: str, info: GraphInfo):
  info.visitados[r] = True
  for v, w in g.listEdges():
    if info.visitados[v] and not info.explorados[makeE(v,w)]:
      info.explorados[makeE(v,w)] = True
      if not info.visitados[w]:
        info.visitados[w], info.descobertos[makeE(v,w)] = True, True
  return info

def makeE(v,w) -> str:
  return f'{v}-{w}'


print(g.listVertices())
print(g.listEdges())
print(BuscaCompleta(g))

