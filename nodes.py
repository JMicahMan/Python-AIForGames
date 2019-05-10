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
       #678
       #345
       #012
    
    def getNeighbors(Node):
        top_neighbor = Node + 3
        bottom_neighbor = Node - 3
        right_neighbor = Node + 1
        left_neighbor = Node - 1
        topRight_neighbor = Node + 4
        topLeft_neighbor = Node + 2
        bottomRight_neighbor = Node - 2
        bottomLeft_neighbor = Node - 4





        



       
       