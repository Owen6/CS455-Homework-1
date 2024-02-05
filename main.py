import random
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
class Node:
    count = 1

    def __init__(self):
        self.x = random.randrange(0,150,1)
        self.y = random.randrange(0,150,1)
        self.id = Node.count
        Node.count += 1

def main():
    nodes = []
    for i in range(100):
        nodes.append(Node())

    k = 1.2
    d = 14

    obj1 = Node()
    #for j in nodes:
    #    print(j.x, j.y, j.id)
    #for j in nodes:
        #plt.scatter(j.x, j.y, label= "Nodes", color= "blue", marker= "^", s=30)
    plt.scatter([obj.x for obj in nodes], [obj.y for obj in nodes], label= "Nodes", color= "blue", marker= "^", s=30)
    for j in nodes:
        circle = Circle((j.x,j.y), radius= k*d, fill= False, color= 'blue')
        plt.gca().add_patch(circle)
    
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.title('Homework 1')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()