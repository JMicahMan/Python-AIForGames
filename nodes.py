'''nodes.py'''


class Node():
    def __init__(self, point):
        self._point = point
    


node_list = []
def main():
   a_node = Node(0)
   for i in range (0,9):
       node_list.append (Node(i))

       #Nodes need the ablitiy to get neighbors and find out the distance between two nodes
       #Adjancent nodes are 10 diagnol nodes are 14
