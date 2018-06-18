import adjList as g
# import adjMatrix as g

def split(str):
  return str.split("\t")
file  = open("graph.txt","r")

lines = int(split(file.readline())[1])

print(lines)

myGraph = g.Graph()

for i in range(lines):
  vertices = split(file.readline().rstrip())
  v1 = vertices[0]
  v2 = vertices[1]
  print("adding ",v1," and ", v2)
  myGraph.AddE(vertices[0],vertices[1])

myGraph.printMe()
myGraph.getNeighborhood('3')