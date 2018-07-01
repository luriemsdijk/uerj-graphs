# procedimento BuscaProfundidade(G: Grafo, v: Inteiro):
#   var P: Pilha ← ∅
#   Visitado[v] ← V
#   empilha(P, (v, PrimeiroViz(v)))
#   enquanto tamanho(P) > 0 faça
#     (v, w) ← desempilha(P)
#     se w > 0 então // há um próximo vizinho
#       empilha(P, (v, PróximoViz(v, w)))
#       se Visitado[w] então
#         se não Explorada[vw] então
#           Explorada[vw] ← V
#         senão
#           Explorada[vw], Descoberta[vw] ← V, V
#           Visitado[w] ← V
#           empilha(P, (w, PrimeiroViz(w)))

# Fica num loop infinito porque nada garante que P.append((w,g.getNeighborhood(w)[0])) dá em um vértice já lido

from importer import *

def BuscaProfundidadeI(g: Graph, v: str):
  P: List[(str,str)] = list()
  info = GraphInfo(g.listVertices(),g.listEdges())
  info.visitados[v] = True
  P.append((v,g.getNeighborhood(v)[0]))
  while len(P) > 0:
    v,w = P.pop()
    print("V,W",v,w)
    if w != '0':
      P.append((v,g.getNeighborhood(v,w)[0]))
      if(info.visitados[w]):
        info.explorados[EKey(v,w)] = True
      else:
        info.explorados[EKey(v,w)], info.descobertos[EKey(v,w)] = True, True
        info.visitados[w] = True
        P.append((w,g.getNeighborhood(w)[0]))
  return info
