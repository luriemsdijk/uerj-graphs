class Queue:
  def __init__(self):
    self.queue = list()

  def __str__(self):
    return self.queue.__str__()

  def insert(self, dataval):
    # Insert method to add element
    if dataval not in self.queue:
      self.queue.insert(0, dataval)
      return True
    return False
# Pop method to remove element

  def pop(self):
    if len(self.queue) > 0:
      return self.queue.pop()
    return ("No elements in Queue!")

  def size(self):
    return len(self.queue)
