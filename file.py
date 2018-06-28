from adjList import *
# from adjMatrix import *


def getFile():
  def split(str):
    return str.split("\t")
  file  = open("graph.txt","r")

  lines = int(split(file.readline())[1])

  print(lines)

  myGraph = Graph()

  for i in range(lines):
    vertices = split(file.readline().rstrip())
    v1 = vertices[0]
    v2 = vertices[1]
    print("adding ",v1," and ", v2)
    myGraph.AddE(vertices[0],vertices[1])

  myGraph.printMe()
  print("neigh 1: ", myGraph.getNeighborhood('1'))
  print("neigh 2: ", myGraph.getNeighborhood('2'))
  print("neigh 3: ", myGraph.getNeighborhood('3'))
  print("neigh 4: ", myGraph.getNeighborhood('4'))
  print("neigh 5: ", myGraph.getNeighborhood('5'))

  return myGraph


def testCode():
  myGraph = Graph()

  myGraph.AddV('a')
  myGraph.AddV('b')
  myGraph.AddV('c')
  myGraph.AddV('d')

  myGraph.AddE('a','b')
  myGraph.AddE('b','c')
  myGraph.AddE('c','d')
  myGraph.AddE('d','a')



  # myGraph.RemoveV('c')
  # myGraph.AddE('b','c')

  myGraph.printMe()
  print("neighbors a: ", myGraph.getNeighborhood('a'))
  print("neighbors b: ", myGraph.getNeighborhood('b'))
  print("neighbors c: ", myGraph.getNeighborhood('c'))
  print("neighbors d: ", myGraph.getNeighborhood('d'))

# testFile()