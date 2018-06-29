
from typing import Dict
class GraphInfo():
  def __init__(self: 'GraphInfo'):
    self.visitados: Dict[str,bool] = {}
    self.descobertos: Dict[str,bool] = {}
    self.explorados: Dict[str,bool] = {}

  def __str__(self: 'GraphInfo'):
    out:str = "visitados: " + {k for k, v in self.visitados.items() if v}.__str__()
    out += "\n"
    out += "descobertos:" + {k for k, v in self.descobertos.items() if v}.__str__()
    out += "\n"
    out += "explorados:" + {k for k, v in self.explorados.items() if v}.__str__()
    return out
