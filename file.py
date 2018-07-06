from importer import *

filePath = "c:/Users/junde/Documents/UERJ/uerj-graphs/graph.txt"

def split(str):
  return str.split("\t")

def readGraph() -> Graph:
  file  = open(filePath,"r")
  file.readline()
  myGraph = Graph()
  while(True):
  # for i in range(10):
    line = file.readline()
    if(line == ''): break
    if(line[0] == '#'): continue
    vertices = split(line.rstrip())
    myGraph.AddE(vertices[0],vertices[1])
  return myGraph
