from importer import *

# procedimento Busca(G: Grafo):
# rotular (V(G), Visitado: Lógico)
# rotular (E(G), Explorada: Lógico)
# rotular (E(G), Descoberta: Lógico)
# Visitado[V(G)] ← F; Explorada[E(G)] ← F; Descoberta[E(G)] ← F
# r ← 1 // raiz pode ser qualquer vértice
# Busca(G, r)

# procedimento Busca(G: Grafo, r: Inteiro):
# Visitado[r] ← V
# para vw ∈ E(G) tal que Visitado[v] e não Explorada[vw] faça
# Explorada[vw] ← V
# se não Visitado[w] então
# Visitado[w], Descoberta[vw] ← V, V

g = readGraph()

def Busca(g: Graph):
  info = GraphInfo()
  for v in g.listVertices():
    info.visitados[v] = False
  for v, w in g.listEdges():
    info.explorados[makeE(v,w)] = False
    info.descobertos[makeE(v,w)] = False
  r = '1'
  return Busca2(g,r, info)

def Busca2(g: Graph, r: str, info: GraphInfo):
  info.visitados[r] = True
  for v, w in g.listEdges():
    if info.visitados[v] and not info.explorados[makeE(v,w)]:
      info.explorados[makeE(v,w)] = True
      if not info.visitados[w]:
        info.visitados[w], info.descobertos[makeE(v,w)] = True, True
  return info


print(g.listVertices())
print(g.listEdges())
print(Busca(g))

