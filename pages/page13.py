# função EhArvore(G: Grafo): Lógico
# retornar EhConexo(G) e não TemCiclo(G)
from importer import *

def EhArvore(g: Graph) -> bool:
  return EhConexo(g) and not TemCiclo(g)
