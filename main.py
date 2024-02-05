import random
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import math

GLOBAL_k = 1.2
GLOBAL_d = 14
GLOBAL_r = GLOBAL_k*GLOBAL_d

class Node:
    count = 1

    def __init__(self):
        self.x = random.randrange(0,150,1)
        self.y = random.randrange(0,150,1)
        self.id = Node.count
        self.neighbors = []
        Node.count += 1

def main():
    nodes = []
    for i in range(100):
        nodes.append(Node())

    #for j in nodes:
    #    print(j.x, j.y, j.id)
    #for j in nodes:
        #plt.scatter(j.x, j.y, label= "Nodes", color= "blue", marker= "^", s=30)
    
    
    
    findNeighbors(nodes)
    #Print Neighbors, delete later and output to a table
    for k in nodes:
        print(k.id, "neighbors: ", k.neighbors, '\n')

    #print(nodes[1].x, nodes[1].y, nodes[2].x, nodes[2].y, calcDistance(nodes[1], nodes[2]))
    
    plt.subplot(1,2,1)
    plt.scatter([obj.x for obj in nodes], [obj.y for obj in nodes], label= "Nodes", color= "red", marker= "^", s=30)
    for j in nodes:
        circle = Circle((j.x,j.y), radius= GLOBAL_r, fill= False, color= 'blue', linewidth= .5)
        plt.gca().add_patch(circle)
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.title('Homework 1')
    plt.axis('equal')
    plt.legend()

    plt.subplot(1,2,2)
    plt.scatter([obj.x for obj in nodes], [obj.y for obj in nodes], label= "Nodes", color= "red", marker= "^", s=30)
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.title('Homework 1')
    plt.axis('equal')
    plt.legend()
    
    plt.tight_layout()

    plt.show()

def findNeighbors(objs):
    for i in objs:
        for j in objs:
            if i.id == j.id:
                continue
            dist = calcDistance(i,j)
            if dist < GLOBAL_r:
                i.neighbors.append(j.id)


def calcDistance(obj1, obj2):
    return math.sqrt((obj1.x-obj2.x)**2 + (obj1.y-obj2.y)**2)

if __name__ == '__main__':
    main()