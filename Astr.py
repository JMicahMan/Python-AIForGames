import math

'''Astr.py'''
#Node Graph
# 20,21,22,23,24
# 15,16,17,18,19
# 10,11,12,13,14
#  5, 6, 7, 8, 9
#  0, 1, 2, 3, 4

class Node(object):
    def __init__(self, id):
        self._id = id
#Create Nodes using a for loop
#Nodes
NodeList = []



def MakeNodes():
    for i in range (0, 25):
        NodeList.append(Node(i))




def MakeCurrent():

    Node_Current = Node(6)



#Neighboor finding



def getNeighbor(node ,columns = 5):
    right = node._id + 1
   # left = node._id - 1
    top = node._id + columns
    #bottom = node._id - columns
    #TODO: accommodate for non-existent nodes
    return [NodeList[right],NodeList[top]]

MakeNodes()

expected = [NodeList[5],NodeList[1]]

print (getNeighbor(NodeList[0]))



#Node Scoring



#open, current, closed lists
