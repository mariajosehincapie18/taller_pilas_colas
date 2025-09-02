import random

class Queue:

  def __init__(self):
    self.__items = []


  def enqueue(self,e):
    self.__items.append(e)
    return True

  def dequeue(self):
    if self.is_empty():
      return "Error, no hay elementos para retornar"

    return self.__items.pop(0)

  def is_empty(self):
    return len(self.__items) == 0

  def len(self):
    return len(self.__items)

  def first(self):
     if self.is_empty():
      return "Error, no hay elementos para retornar"

     return self.__items[0]

  def __str__(self):
    return '\n'.join(map(str,self.__items))

  def generate(self,num, min, max):
   for i in range(0,num):
    self.enqueue(random.randint(min,max))