
from typing import Dict,List,Tuple
from misc import EKey

class GraphInfo():
  def __init__(self: 'GraphInfo', vertices: List[str] = None,edges: List[Tuple[str,str]] = None):
    self.visitados: Dict[str,bool] = {}
    self.descobertos: Dict[str,bool] = {}
    self.explorados: Dict[str,bool] = {}
    self.distancias: Dict[str,int] = {}

    if(vertices):
      for v in vertices:
        self.visitados[v] = False
        self.distancias[v] = 0
    if(edges):
      for v, w in edges:
        self.explorados[EKey(v,w)] = False
        self.descobertos[EKey(v,w)] = False

  def __str__(self: 'GraphInfo'):
    out:str = "visitados: " + {k for k, v in self.visitados.items() if v}.__str__()
    out += "\n"
    out += "descobertos:" + {k for k, v in self.descobertos.items() if v}.__str__()
    out += "\n"
    out += "explorados:" + {k for k, v in self.explorados.items() if v}.__str__()
    return out
