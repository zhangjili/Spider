# -*- coding: gbk-*-
import os
path = os.path.dirname(__file__)
print(path)
# path = os.path.dirname(os.path.dirname(__file__))
# print(path)
# print(os.path.exists(path))
from queue import Queue

q = Queue()
q.put(("fdf","122"))
print(q.get())