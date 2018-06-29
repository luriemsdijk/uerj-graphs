from node import *
from typing import List

class Graph:
  def __init__(self: 'Graph', vertices: List[str] = []):
      self.list: List[Node] = []
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
    vertices = self.getInOrder(v1,v2)
    if (not self.exists(v1) ):
      self.AddV(v1)

    if (not self.exists(v2) ):
      self.AddV(v2)

    self.getVertice(vertices[0]).insert(vertices[1])

  def RemoveE(self, v1, v2):
    vertices = self.getInOrder(v1,v2)
    vertices[0].remove(vertices[1])

  def getNeighborhood(self, vertex):
    neighbors = []
    for v in self.list:
      if(v.name == vertex):
        neighbors = neighbors + v.getList()
      else:
        if(v.contains(vertex)):
          neighbors.append(v.name)
    return neighbors
