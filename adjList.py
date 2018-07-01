from node import *
from typing import List
from misc import EKey

print("Adjecency as List")

class Graph:
  def __init__(self: 'Graph', vertices: List[str] = []):
      self.list: List[LinkedList] = []
      self.vNames: List[str] = []
      for v in vertices:
        self.AddV(v)

  def getVertice(self,vName):
    for v in self.list:
      if(v.name == vName):
        return v

  def exists(self, vName):
    for v in self.list:
      if(v.name == vName):
        return True
    return False

  def listVertices(self: 'Graph') -> List[str]:
    return self.vNames

  def listEdges(self: 'Graph'):
    edges = []
    for index,linked in enumerate(self.list):
      for incident in linked.getList():
        # edges.append(f'{self.vNames[index]}-{incident}')
        edges.append([self.vNames[index],incident])
    return edges

  def getInOrder(self, v1Name, v2Name):
    v1 = v1Name
    v2 = v2Name

    first = v1 if v1 < v2 else v2
    second = v1 if v1 > v2 else v2

    return [first,second]

  def AddV(self, v1: str):
    self.vNames.append(v1)
    self.list.append(LinkedList(v1))

  def RemoveV(self, v1):
    self.vNames.remove(v1)
    for v in self.list:
        if(v.name == v1):
          self.list.remove(v)
          continue
        v.remove(v1)

  def printMe(self: 'Graph'):
    for v in self.list:
        print("printMe: ",v.name,v)

  def AddE(self, v1, v2):
    v1,v2 = self.getInOrder(v1,v2)
    if (not self.exists(v1) ):
      self.AddV(v1)

    if (not self.exists(v2) ):
      self.AddV(v2)

    self.getVertice(v1).insert(v2)

  def RemoveE(self, v1, v2):
    vertices = self.getInOrder(v1,v2)
    vertices[0].remove(vertices[1])

  def getNeighborhood(self: 'Graph', vertex:str, excpt: str = '') -> str:
    neighbors = []
    for v in self.list:
      if(v.name == vertex):
        neighbors = neighbors + v.getList()
      else:
        if(v.contains(vertex)):
          neighbors.append(v.name)
    if excpt in neighbors: neighbors.remove(excpt)
    return neighbors if neighbors else ['0']

  def __str__(self: 'Graph'):
    out:str = "Vertices: " + sorted(self.listVertices(),key=str.lower).__str__()
    out += "\n"
    out += "Arestas:" + sorted({ EKey(v,w) for v,w in self.listEdges()},key=str.lower).__str__()
    return out
