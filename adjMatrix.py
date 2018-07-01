import numpy as np
from typing import List

print("Adjecency as Matrix")
class Graph:
  def __init__(self, vertices: List[str] = []):
    self.n = len(vertices)
    self.vertices = vertices
    self.matrix = np.zeros((self.n,self.n))

  def getVertice(self,i):
    if(i < len(self.vertices)):
      return self.vertices[i]
    return -1

  def listVertices(self: 'Graph'):
    return self.vertices

  def listEdges(self: 'Graph'):
    edges = []
    for (rIndex, row) in enumerate(self.matrix):
      for (cIndex, col) in enumerate(row):
        if(col == 1):
        #   edges.append(f'{rIndex}-{cIndex}')
          edges.append([rIndex,cIndex])
    return edges

  def getIndexesAndOrder(self, v1Name, v2Name):
    v1 = self.vertices.index(v1Name)
    v2 = self.vertices.index(v2Name)

    v1Index = v1 if v1 < v2 else v2
    v2Index = v1 if v1 > v2 else v2
    return [v1Index,v2Index]


  def AddV(self, v1):
    if v1 in self.vertices:
      return False
    self.vertices.append(v1)
    self.matrix = np.append(self.matrix, np.zeros((self.n,1)), axis=1)
    self.n += 1
    self.matrix = np.append(self.matrix, np.zeros((1,self.n)), axis=0)
    return True

  def RemoveV(self, v1):
    if v1 not in self.vertices:
      return False

    v1Index = self.vertices.index(v1)
    self.vertices.remove(v1)
    self.matrix = np.delete(self.matrix, v1Index, axis=1)
    self.matrix = np.delete(self.matrix, v1Index, axis=0)
    self.n -= 1
    return True

  def printMe(self: 'Graph'):
    if(len(self.matrix)):
      for v in self.vertices:
        index = int(v)-1
        self.matrix[index][index] = 9
    print(self.vertices)
    print(self.matrix)

  def AddE(self, v1, v2):
    if(v1 not in self.vertices):
      self.AddV(v1)
    if(v2 not in self.vertices):
      self.AddV(v2)
    vertices = self.getIndexesAndOrder(v1,v2)
    self.matrix[vertices[0]][vertices[1]] = 1

  def RemoveE(self, v1, v2):
    if(v1 not in self.vertices and v2 not in self.vertices):
      return False

    vertices = self.getIndexesAndOrder(v1,v2)
    self.matrix[vertices[0]][vertices[1]] = 0

  def getNeighborhood(self: 'Graph', vertex:str, excpt: str = '') -> List[str]:
    if( vertex not in self.vertices):
      return []
    vIndex = self.vertices.index(v)
    neighbors = []
    for i in range(vIndex,self.n):
      if(self.matrix[vIndex][i] == 1):
        neighbors.append(self.getVertice(i))

    for i in range(vIndex,-1,-1):
      if(self.matrix[i][vIndex] == 1):
        neighbors.append(self.getVertice(i))
    if excpt in neighbors: neighbors.remove(excpt)
    return neighbors if neighbors else ['0']

  def __str__(self: 'Graph'):
    out:str = "Vertices: " + self.listVertices().__str__()
    out += "\n"
    out += "Arestas:" + { EKey(v,w) for v,w in self.listEdges()}.__str__()
    return out
