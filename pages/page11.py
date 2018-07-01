# função EhFloresta(G: Grafo): Lógico
# retornar não TemCiclo(G)

from importer import *

def EhFloresta(g: Graph):
  return not TemCiclo(g)
