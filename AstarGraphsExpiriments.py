'''AstarGraphsExpiriments.py'''

import collections
#from implementation import *


# 0,1,2
# 3,4,5
# 6,7,8

class Graph():
    def __init__(self):
        self.edges = {}

    def neighbors(self, id):
        return self.edges[id]
    
exmpl = Graph()
exmpl.edges = { '0':['3','4','1'],
                '1':['0','3','4','5','2'],
                '2':['1','4','5'],
                '3':['0','1','4','7','6'],
                '4':['0','1','2','3','5','6','7','8'],
                '5':['2','1','4','7','8'],
                '6':['3','4','7'],
                '7':['6','3','4','5','8'],
                '8':['5','4','7']}

class Line:
    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements) == 0
    
    def put(self, x):
        self.elements.append(x)

    def get(self):
        return self.elements.popleft()

def breadth_first_search_1(graph, start):
    frontier = Line()
    frontier.put(start)
    visited = {}
    visited[start] = True 

    while not frontier.empty():
        current = frontier.get()
        print("Visiting %r" % current)
        for next in graph.neighbors(current):
            if next not in visited:
                frontier.put(next)
                visited[next] = True
breadth_first_search_1(exmpl, '0')

def breadth_first_search_2(graph, start):
    #return "came_from"
    frontier = Line()
    frontier.put(start)
    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()
        for next in graph.neighbors(current):
            if next not in came_from:
                frontier.put(next)
                case_from[next] = current
    
    return came_from

def breadth_first_search_3(graph, start, goal):
    frontier = Line()
    frontier.put(start)
    came_from = {}
    came_[start] = None

    while not frontier.empty():
        current = frontier.get():

        if current == goal:
            break

        for next in graph.neighbors(current):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current
    
    return came_from


class SqrGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []
    def in_bounds(self, id):
        (x,y) = id
        return 0 <= x < self.width and 0 <= y < self.height
    def passable(self, id):
        return id not in self.walls
    def neighbors(self, id):
        (x,y) = id
        results = [(x+1, y),(x, y-1),(x-1,y),(x, y+1)]
        if (x+y)%2==0: results.reverse() # aesthetics
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results

    
class GridWithWeights(SqrGrid):
    def __init__(self, width, height):
        super().__init__(width,height)
        self.weights = {}

    def cost(self, from_node, to_node):
        return self.weights.get(to_node, 1)
        