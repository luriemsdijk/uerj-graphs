from typing import List

def EKey(v,w) -> str:
  return f'{v}-{w}' if v < w else f'{w}-{v}'

def EFromKey(edge: str) -> List[str]:
  return edge.split('-')
